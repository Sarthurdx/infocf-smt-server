<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page import="java.text.*" %>
<%@ page import="java.util.*" %>

<%@ page import = "java.io.*,java.util.*, javax.servlet.*" %>
<%@ page import = "javax.servlet.http.*" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
		<title>InfOCF+W - Lehrgebiet Wissensbasierte Systeme</title>
		<link href="Style.css" rel="stylesheet">
		<link rel='icon' href='favicon.ico' type='image/x-icon'/ >
		<script src="jQuery.min.js" type="text/javascript"></script>
		<script src="app-ajax.js" type="text/javascript"></script>
		

	</head>
	<body>
		<div id="gui">
			<div id=head>
				<div id=logowrapper><img id=logo src="logo.png" /><br>
				<a target="_blank" href="https://fernuni-hagen.de/wbs/">Knowledge Based Systems</a><br>
				Prof. Dr. Christoph Beierle</div>
				<h1>InfOCF+W</h1>
				<b>A tool for reasoning with conditional knowledge bases</b><br>
			</div>
			<div id="knowledgebase_wrapper">
				<div id="knowledgebase_head"><h2>Conditional belief base</h2></div>
				<div id="knowledgebase_body">
					
					<textarea id="knowledgebase"></textarea>
					<p><strong>Syntax:</strong> conjunction: "a,b"; disjunction "a;b"; negation "!a"; brackets ((a;b),a); tautology: Top; contradiction: Bottom</p>   
					<input id=demobtn onclick="demo()" type=button value="Load demo"/>
					<div class="upload-btn-wrapper">
					<button class="btn">Load knowledge base from .cl file</button>
						<input type="file" id="files" name="files[]" multiple /><br>
					</div>
					
					<output id="list"></output><br>
					
				</div>
			</div>
		
			<div id="r_func" style="width:69%; margin-left: 1%">
				<div id="r_func_head"><h2>Representation (for the conditional belief base)</h2><div style="display:none"  onclick="toggle('r_func')" class=close>Close</div></div>
				<div id="r_func_conf">			
					<div>
						<h2>Choose representation to compute</h2>
						<input name=ModelSetKind onclick="changeRadio()" checked=checked value="CREP_CW" type=radio />cw-minimal c-representations<br>
						<input name=ModelSetKind onclick="changeRadio()" value="CREP_SUM" type=radio />sum-minimal c-representations<br>
						<input name=ModelSetKind onclick="changeRadio()" value="CREP_IND" type=radio />ind-minimal c-representations<br>
						<input name=ModelSetKind onclick="changeRadio()" value="SYSTEM_Z" type=radio />System Z<br>
					</div>
					<div>
						<h2>Maximal impact (for c-representations)</h2>
						<input name=MaximalImpactRF checked=checked value="0" type=radio  />Unbounded<br>
						<input name=MaximalImpactRF value="1" type=radio  />Number of conditionals<br>
						<input name=MaximalImpactRF value="2" type=radio  />Exponential in number of conditionals<br>
						<input name=MaximalImpactRF value="3" type=radio  />Manual <input type="number" value="0" name="MaximalImpactRFNr"  /><br>
						<!--  <input type=button value="Save OCFS"/>-->
						<br>
						<input type=button id=btn_calc_rfunc value="Compute"/>
						<!--  <button onclick="svdownload();">Download results</button> -->
					</div>
				</div>
				<div id="r_func_result">
					<div>
						<h2>Solutions</h2>
						<div id=result_list></div>
					</div>
					<div>
						<div id=result></div>
					</div>
				</div>
				
			</div>
		
			<div id="query">
				<div id="query_head"><h2>Query (with respect to the conditional belief base)</h2><div  onclick="toggle('query')" class=close>Close</div></div>
				<div id="query_conf">
					<div class=hg>
					
					<div class=quater>   
						<h2>Other inference systems</h2>
						<input name="Models" value="SYSTEM_P" type="checkbox">System P<br>
						<input name="Models" value="SYSTEM_Z" type="checkbox">System Z<br>
						<input name="Models" value="SYSTEM_W" type="checkbox">System W<br>
					</div>
					<div class=threeq>
					<h2>Inference with c-representations</h2>
					<div class=third>
						<input name=crep value="CREP_ALL" type=checkbox checked=checked />all<br>
						<input name=crep value="CREP_CW" type=checkbox />cw-minimal<br>
						<input name=crep value="CREP_SUM" type=checkbox />sum-minimal<br>
						<input name=crep value="CREP_IND" type=checkbox />ind-minimal<br>
						
						
					</div>
					<div class="third border" >
						<h2>Maximal impact</h2>
						<input name=MaximalImpactQ checked=checked value="0" type=radio />number of conditionals<br>
						<input name=MaximalImpactQ value="1" type=radio />number of conditionals<br>
						<input name=MaximalImpactQ value="2" type=radio />exponential of conditionals<br>
						<input name=MaximalImpactQ value="3" type=radio />manual <input type="number" value="0" name="MaximalImpactQNr"  /><br>
					</div>
					<div class=third>
						<h2>Inference mode</h2>
						<input name=Mode checked=checked value="SKEPTICAL" type=checkbox />skeptical<br>
						<input name=Mode value="WEAKLY_SKEPTICAL" type=checkbox />weakly skeptical<br>
						<input name=Mode value="CREDULOUS" type=checkbox />credulous<br>
					</div>
					</div>
					</div>
					
					<div class=full>
						<h2>Query</h2>
						<input name=query1 type=text /> entails <input name=query2 type=text /> 
	
						<input type=button id=btn_calc_query value="Answer"/>
						<!-- <button onclick="download($('#result_q table'),'', 'query.csv');">Download results</button> -->
						<div id=querysystems></div>


					</div>
				</div>
				<div id="query_result">
					<div>
						<h2>Query results for inference based on c-representations</h2>
						<div id=result_q></div>
					</div>
				</div>
			</div>
		</div>
		<div class="modal"><div style="width: 300px;position: relative;margin-left: auto;margin-right: auto;margin-top: 20px;text-align: center;font-weight: bold;">
Please wait - the time limit is 30 min.</div></div>
	</body>


</html>
