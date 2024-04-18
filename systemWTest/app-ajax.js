var globalSignature = [];
	var globalConditionals = [];
	var globalConditionalsName = '';
	
$(document).ready(function() {
	
	
	$body = $("body");
	$.ajaxSetup({
		timeout:1800000,
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			if (textStatus == 'timeout') {
				//alert('The calculation has caused a timeout exception (90s).');
				alert('I am sorry - the computation reached the runtime limit of InfOCF-Web. Please use InfOCF-Lib instead.');				 
			} else {
				alert('There has been an error executing the Servlet.');
			}
		}
	});
	$(document).on({
	    ajaxStart: function() { $body.addClass("loading");    },
	     ajaxStop: function() { $body.removeClass("loading"); }    
	});
	if (window.File && window.FileReader && window.FileList && window.Blob) {
  
	} else {
	  alert('The File APIs are not fully supported in this browser.');
	}


 
	//Handler for the OCFs calculationbutton 
	$('#btn_calc_rfunc').on('click', function() {
		var knowledgebase = $('#knowledgebase').val();
		
		//remove comments
		//knowledgebase = knowledgebase.replace(/^\/\/.*\n?/mg, '');
		//knowledgebase = knowledgebase.replace(/^#.*\n?/mg, '');
		
		knowledgebase = knowledgebase.replace(/\/\*[\s\S]*?\*\/|\/\/.*/g,'');
		
		tmpkb = validateKnowlegeBase(knowledgebase);
		
		
		console.log(tmpkb);
		
		if (tmpkb == false) {
			return false;
		} else {			
		//$('#knowledgebase').val(tmpkb);
			var knowledgebase = tmpkb;
			var modelkind = $("#r_func input[name='ModelSetKind']:checked").val();
			var maximalimpact = $("#r_func input[name='MaximalImpactRF']:checked").val();
			var maximalimpactnr = $("#r_func input[name='MaximalImpactRFNr']").val();
			if (modelkind == "SYSTEM_W") {
			    $.get('StructureOnWorldsServlet', {
					knowledgebase : knowledgebase
				}, function(responseText) {
					if (responseText.trim() !== '') {
						$('#r_func_result').replaceWith(responseText);
					}
					else {
						alert('Error: Something went wrong while calculating the preferred structure on worlds.');
					}
				});
			}
			else {
				backend = 'http://wbs2.fernuni-hagen.de:18085/polls/'
				$.get(backend+'consistency', {
					knowledgebase : knowledgebase,
					modelkind : modelkind,
					maximalimpact: maximalimpact,
					maximalimpactnr : maximalimpactnr
				}, function(responseText) {
						if (responseText.trim() == 'true') {
							// Call servlet
							
							backend = 'http://wbs2.fernuni-hagen.de:18085/polls/'
							folder = 'cw/'

							$.get(backend+'cw/', {
								knowledgebase : knowledgebase,
								modelkind : modelkind,
								maximalimpact: maximalimpact,
								maximalimpactnr : maximalimpactnr
							}, function(responseText) {
									if (responseText.trim() !== '') {
										$('#r_func_result').replaceWith(responseText);

										if (modelkind == 'SYSTEM_Z') {
											$.get(backend+'partition/', {
												knowledgebase : tmpkb
											}, function(responseText) {
													console.log(responseText);
													$('#result_list').html(responseText);
											});
										}
									} else {
										alert('Error: There is no solution for the given maximal impact of '+maximalimpactnr+'!');
									}
							});
						} else {
							alert('Error: The knowlegebase is not consistent!');
							return false;
						}
				});
			}
		  
		}	
	});
	
	
	//Handler for the querybutton
	$('#btn_calc_query').on('click', function() {
		
		
		var knowledgebase = $('#knowledgebase').val();
		
		//remove comments
		//knowledgebase = knowledgebase.replace(/^\/\/.*\n?/mg, '');
		//knowledgebase = knowledgebase.replace(/^#.*\n?/mg, '');
		
		knowledgebase = knowledgebase.replace(/\/\*[\s\S]*?\*\/|\/\/.*/g,'');
		
		knowledgebase = validateKnowlegeBase(knowledgebase);
		
		
		var systems = $("#query input[name='Models']:checked").map(function(){
			return $(this).val();
		}).get();
		var system = systems.join(';');
		var creps = $("#query input[name='crep']:checked").map(function(){
			return $(this).val();
		}).get();
		
		var crep = creps.join(';');
		if (crep == '')
			crep = 'NONE';
		var maximalimpact = $("#query input[name='MaximalImpactQ']:checked").val();
		var maximalimpactnr = $("#query input[name='MaximalImpactQNr']").val();
		
		var modes = $("#query input[name='Mode']:checked").map(function(){
			return $(this).val();
		}).get();
		
		var mode = modes.join(';');
		if (mode == '')
			mode = 'SKEPTICAL';
		
		var query1 = $("#query input[name='query2']").val();
		var query2 = $("#query input[name='query1']").val();
		
		
		query1 = query1.replace(/\s/g,'');
		query2 = query2.replace(/\s/g,'');
		
		if (!checkConditionalForQuery(query1)) {
			return;
		};
		if (!checkConditionalForQuery(query2)) {
			return;
		};
		
		
		if (knowledgebase === '') {
			alert('Missing knowledgebase');
			return;
		}
		
		tmpkb = validateKnowlegeBase(knowledgebase);
		
		
		console.log('Out start');
		console.log(query1);
		console.log(query2);
		console.log(tmpkb);
		console.log('Out end');
		if (!checkConditionalVariables(query1, globalSignature, "Query")) {
			return;	
			
		}
		if (!checkConditionalVariables(query2, globalSignature, "Query")) {
			return;	
			
		}
		
		if (!/^[!TBa-z,;() ]+$/.test(query1)) {
			alert('Check conclusion of the query');
			return;			
		}
		
		if (!/^[!TBa-z,;() ]+$/.test(query2)) {
			alert('Check premise of the query');
			return;			
		}
		
		if (query1 === '' | query2 === '') {
			alert('Missing query parameters');
			return;
		}
		
		
		//servlet call
		backend = 'http://wbs2.fernuni-hagen.de:18085/polls/inference/'
		$.get(backend, {
			knowledgebase : tmpkb,
			system : system,
			crep : crep,
			query2 : query2,
			query1 : query1,
			mode : mode,
			maximalimpact: maximalimpact,
			maximalimpactnr : maximalimpactnr
		}, function(responseText) {
				if (responseText !== '') {
			var results = responseText.split('EOD');
				$('#result_q').html(results[0]);
				$('#result_w').html(results[1]);
				if (results[1] !== '')
				$('#querysystems').replaceWith(results[1]);
		}
				
		});


	});
	
	// 
	function handleFileSelect(evt) {
		var files = evt.target.files;
		var output = [];
		for (var i = 0, f; f = files[i]; i++) {
			var fr = new FileReader(); 
			fr.onload = function(e) { 
				var conditionalC = (e.target.result.split("(").length - 1);
				$("input[name='MaximalImpactQNr']").val(conditionalC);
				$("input[name='MaximalImpactRFNr']").val(conditionalC);
				$('#knowledgebase').val(e.target.result);
			}; 
			fr.readAsText(f);
		}
		document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
	}


	document.getElementById('files').addEventListener('change', handleFileSelect, false);
	
});





function validate(knowledgebase) {
	if (knowledgebase === '') {
		alert('Missing knowledgebase');
		return false;
	}
}

function bracketValidate(input) {
  let tmp = 0;
  for (c of input) {
    if (c === '(') tmp++;
    else if (c === ')' && --tmp < 0) return false; // Unexpected  ')' 
  }
  return tmp === 0; // False if unbalanced
}

function getPartition() {
	
		$.get('PartitionsServlet', {
			knowledgebase : knowledgebase

		}, function(responseText) {
				console.log(responseText);
				
		});
}



// toggle panel
function toggle(id) {
	if ($('#'+id).height() == '44') {
		$('#'+id).height('auto');
		$('#'+id+ ' .close' ).html('Close');
	} else {
		$('#'+id).height('44');
		$('#'+id+ ' .close' ).html('Open');
	}
}

// write demo for OCFs
function demo() {
	$('#knowledgebase').val(`

signature
  a,b,c

conditionals
kb_056c{
  (b|a),
  (!a,!b|!a;!b),
  (c|Top)
}
`);

	$('input[name=query1]').val("!a,b;a,!b");
	$('input[name=query2]').val("!a,b");
}

function changeRadio() {
    if ($('input[type=radio][id=systemzradio]').is(':checked') | $('input[type=radio][id=systemwradio]').is(':checked')) {
        $( "input[type=radio][name=MaximalImpactRF]" ).prop( "disabled", true );
    } else {
		$( "input[type=radio][name=MaximalImpactRF]" ).prop( "disabled", false );
	}
}

function toggleTable(id) {
	$('#result table').hide();
	$('#result #table_'+id).show();
}
function toggleAllTable() {
	$('#result table').show();
}

function svdownload() {
	toggleAllTable();
	result_tables = $('#result table');
	result_list = $('#result_list table');
	
	
	
	solution_tables = $('#result_table ul');
	
	$.each(result_tables, function(index, value) {
		$(value).find(' th:last').after('<th style="display:none">'+$('#option_'+(index+1)+' span:last').html()+'</th>');
	});
	download(result_tables, result_list, 'OCFs.csv');
}//end svdownload


function download(data, result_list, filename) {
	console.log(data);
	console.log(result_list);

	if (result_list !== '') {
		result_list = exportTableCSV(result_list);
	}
	data = exportTableCSV(data);
	
	console.log(data);
	console.log(result_list);
	data = data + "\r\n\r\n" + result_list;
    var file = new Blob([data], {type: "application/csv"});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);  
        }, 0); 
    }
}//end download

// export data as csv
function exportTableCSV($table) {

    var $rows = $table.find('tr:has(td),tr:has(th)'),
	tmpColDelim = String.fromCharCode(11), 
        tmpRowDelim = String.fromCharCode(0), 
        colDelim = '","',
        rowDelim = '"\r\n"',
 csv = '"' + $rows.map(function (i, row) {
            var $row = $(row), $cols = $row.find('td,th');

            return $cols.map(function (j, col) {
                var $col = $(col), text = $col.text();

                return text.replace(/"/g, '""'); // escape double quotes

            }).get().join(tmpColDelim);

        }).get().join(tmpRowDelim)
            .split(tmpRowDelim).join(rowDelim)
            .split(tmpColDelim).join(colDelim) + '"',



    // Data URI
    csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(csv);
	return csv;
}//end exportTableCSV








/*

*/
function validateKnowlegeBase(line) {
	var cleanstring = '';
	var signature = '';
	var conditionals = '';
	
	
	if (!bracketValidate(line)) {
		alert('Error: There is a syntax error in the knowledge base.');
		return false;
	}
	
	line = line.replace(/#/g,'');
	
	

	
	if (line == '') {
		alert('Error: The knowlegebase is empty!');
		return false;
	}

	if (!line.match(/signature/ig)) {
		alert("Error: The signature is empty!");
		return false;
	}

	if (!line.match(/conditionals/ig)) {
		alert("Error: No conditionals found!");
		return false;
	}
	
	var count = (line.match(/signature/ig) || []).length;
	if (count > 1) {
		alert("Error: More than one signature!");
		return false;
	}
	count = (line.match(/conditionals/ig) || []).length;
	if (count > 1) {
		alert("Error: More than one conditional blocks!");
		return false;
	}

	line = line.replace(/^\s*[\r\n]/gm, '');
	line = line.replace(/(\r\n|\n|\r)/gm, '\n');
	line = line.split('\n');
	var cursor = '';
	
	//Remove Comments
	
	for(var i = 0;i < line.length;i++){
		
		
		
		if (line[i].trim().match(/signature/i)) {
			if (line[i].trim().replace(/signature/gm, '') !== '' ) {
				alert("Error: The keyword signature must be on a single line!");
				return false;
			} else {
				cursor = 'signature';			
			}
		} 
		
		if (line[i].trim().match(/conditionals/i)) {
			if (line[i].trim().replace(/conditionals/gm, '') !== '' ) {
				alert("Error: The keyword conditionals must be on a single line!");
				return false;
			} else {
				cursor = 'conditionals';			
			}
		} 
		
		
		
		
		
		
		if (cursor == 'conditionals') {
				conditionals += line[i].replace(/conditionals/gm, '').trim()+' ';
		} else if (cursor == 'signature') {
				signature += line[i].replace(/signature/gm, '').trim()+' ';
		}
		cleanstring += line[i].trim()+' ';
		
		
	}
	
	
	
	globalSignature    = checkSignature(signature);
	
	if (globalSignature == false)
		return false;
	
	
		
	globalConditionals = checkConditionals(conditionals);
	if (globalConditionals == false)
		return false;
	
	console.log('Result:');
	console.log(globalSignature);
	console.log(globalConditionals);
	console.log(globalConditionalsName);
	var out = 'signature\r\n  ';
	
	for(var i = 0;i < globalSignature.length;i++){
		if (i == globalSignature.length-1) {
			out += globalSignature[i]+'\r\n\r\n';
		} else {
			out += globalSignature[i]+',';
		}
	}
	out += 'conditionals\r\n';
	out += globalConditionalsName+'{\r\n';
	
	for(var i = 0;i < globalConditionals.length;i++){
		if (i == globalConditionals.length-1) {
			out += '  ('+globalConditionals[i]+')\r\n}';
		} else {
			out += '  ('+globalConditionals[i]+'),\r\n';
		}
	}
	
	console.log(out);
	return out;
}//end validateKnowlegeBase


/*

*/
function checkConditionals(input) {
	
	
	// Match conditionals list
	line = input.replace(/ /g,'');
console.log("line "+line);
	var regexString = /\{([a-z!,#; \(\)|]+)\}/gi,
    matches;
	matches = regexString.exec(line.trim());
	
	if (matches === null) {
		console.log('conditional '+input);
		alert("There is a syntax error in the query. ("+input+")");
		return false;
	} else {
		strConditionals = matches[1].trim();
	}
	regexString = /^([a-z0-9_]+)[ ]?\{/gi;
	matches = regexString.exec(line.trim());
	
	if (matches === null) {
		alert("Error: Name of conditionals is invalid! ("+line.trim()+")");
		return false;
	} else {
		globalConditionalsName = matches[1].trim();
	}
	
	regexString = /(\([a-z|(),;!]+\))/mig;
	matches = regexString.exec(strConditionals.trim());
	
	level = 0;
	matchedConditionals = [];
	singleConditional = '';
	for(var i = 0;i < strConditionals.length;i++){
		if (level == 0) {
			if (strConditionals[i] !== ',' &  strConditionals[i] !== '(') {
				singleConditional+= strConditionals[i];
			}
		} else {
			singleConditional+= strConditionals[i];
		}
		
		
		if (strConditionals[i] == '(') {
			level += 1;
		}
		if (strConditionals[i] == ')') {
			level -= 1;
			if (level == 0) {

				matchedConditionals.push(singleConditional.replace(/.$/,""));
				singleConditional = '';
			}
		}
	}
	
	
	
	
	var matchesConditionals = [];
	while (matches != null) {
		matchesConditionals.push(matches[1]);
		matches = regexString.exec(strConditionals.trim());
	}
	
	matchesConditionals = matchedConditionals;
	
	
	globalConditionals = [];
	for(var i = 0;i < matchesConditionals.length;i++){
		
		
        if (matchesConditionals[i] == "") { 
			alert("Error: Empty conditionals are not allowed. (" + strConditionals.trim()+')');
			return false;
		} else {
			if (!checkConditionalVariables(matchesConditionals[i], globalSignature, "Knowlege base")) {
				return false;
			}
			
			checkedConditional = checkConditional(matchesConditionals[i]);
		if (checkedConditional == false) {
			return false;
			
		} else {
			
			globalConditionals.push(checkedConditional);
		}
		}
    }
	console.log(globalConditionals);
	
	return globalConditionals;
}//end checkConditionals

/*

*/
function checkConditionalVariables(conditional, signature, source) {
	conditional = conditional.replace(/[()]/g, "");
	
	conditional = conditional.replace(/ /g,'');
	
	var list = conditional.split(/[|,!;]+/);
	

	
	let checker = (arr, target) => target.every(v => arr.includes(v));
	var filtered = list.filter(function (el) {
		return (el != null & el != '');
	});
	
	signatureTMP = signature.slice(0);
	signatureTMP.push("Top");
	signatureTMP.push("Bottom");
	
	
	
	check = checker(signatureTMP, filtered);

	
	
	if (check) {
		return true;
	} else {
		
		alert("There is a syntax error in the "+ source.toLowerCase()+".");
		return false;
	}
}//end checkConditionalVariables()

/*

*/
function checkConditional(input) {
	
	
	
	
	var regexString = /^[a-zTB| (),;!]+$/ig;
	var matches = regexString.exec(input.trim());
	
	
	
	
	if (matches === null) {
		alert("Error: There is an error in the conditionals syntax!");
		return false;
	}
	
	var parts = input.split('|');
	for(var i = 0;i < parts.length;i++){
		var list = parts[i].trim().split(/[,;]{1}/);
		for(var u = 0;u < list.length;u++){
			if (list[u] === '') {
				alert("There is a syntax error in a conditional of the knowledge base.");
				return false;
			}
			
			
			
			regexString = /^[!]?[a-zTB|(),;!]+$/ig;
			matches = regexString.exec(list[u].trim());
			
			
			console.log("check list:" + list[u]+".");
	
	console.log(matches);
			
			if (matches === null) {
				alert("Error: Error in conditional: ("+input+")");
				return false;
			}
		}
	}
	return input;
}//end checkConditional



function checkConditionalForQuery(input) {
	
	input = input.replace(/ /g,'');
	
	console.log('input1');
	console.log(input);
	
	
	
	var regexString = /^[a-zTB|(),;!]+$/ig;
	var matches = regexString.exec(input.trim());
	
	
	
	
	if (matches === null) {
		alert("Error: There is an error in the conditionals syntax!");
		return false;
	}
	
	var parts = input.split('|');
	for(var i = 0;i < parts.length;i++){
		var list = parts[i].trim().split(/[,;]{1}/);
		for(var u = 0;u < list.length;u++){
			if (list[u] === '') {
				alert("There is a syntax error in a conditional of the query.");
				return false;
			}
			
			
			
			regexString = /^[!]?[a-z|TB(),;!]+$/ig;
			matches = regexString.exec(list[u].trim());
			
			
	
	
	
			
			if (matches === null) {
				alert("Error: Error in conditional: ("+input+")");
				return false;
			}
		}
	}
	return true;
}//end checkConditional

/*

*/
function checkSignature(line) {
	if (!line.trim().match(/[,a-z]/gmi)) {
		alert("Error: The signature has to be a comma seperated list of labels consisting out of alphabetical characters.");
		return false;
	}
	globalSignature = [];
	var signatureList = line.trim().split(",");
    for(var i = 0;i < signatureList.length;i++){
        if (signatureList[i] == "") { 
			//alert("Error: No empty variables allowed. (" + line.trim()+')');
			alert("There is a syntax error in the knowlege base.");
			return false;
		} else {
		
			globalSignature.push(signatureList[i].trim());
		}  
    }
	
	return globalSignature;
}//end checkSignature()



