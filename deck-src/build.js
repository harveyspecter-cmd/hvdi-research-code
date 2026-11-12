/*
 * Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
 * Contact: bpgp25sushant@iima.ac.in
 *
 * PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
 * reverse engineering, or use of this file, via any medium, is strictly prohibited
 * without the express prior written permission of Sushant Gaurav.
 */
const pptxgen=require("pptxgenjs");
// applyTheme writes the theme colours into the .pptx after pptxgenjs saves it. It is a separate helper that is
// not part of this repository; set HVDI_APPLY_THEME to the path of apply_theme.js before running.
if(!process.env.HVDI_APPLY_THEME){console.error("Set HVDI_APPLY_THEME to the path of apply_theme.js (see README, section 6).");process.exit(1)}
const {applyTheme}=require(process.env.HVDI_APPLY_THEME);
const DARK={name:"HVDI",headFontFace:"Arial",bodyFontFace:"Arial",colors:{dk1:"000000",lt1:"F3F1EA",dk2:"101211",lt2:"9A9D96",accent1:"E8601C",accent2:"3D8FD6",accent3:"B9B5A8",accent4:"232523",accent5:"6B6E68",accent6:"FFFFFF",hlink:"E8601C",folHlink:"B9B5A8"}};
const LIGHT={name:"HVDI Print",headFontFace:"Arial",bodyFontFace:"Arial",colors:{dk1:"FFFFFF",lt1:"141414",dk2:"F3F2ED",lt2:"555555",accent1:"C24E12",accent2:"2A6FB0",accent3:"8A867A",accent4:"D5D3CC",accent5:"777777",accent6:"000000",hlink:"C24E12",folHlink:"8A867A"}};
const PRINT=process.env.DECK_THEME==="print";
const THEME=PRINT?LIGHT:DARK;
const OUT=PRINT?"Beyond_the_Hype_Cycle_Deck_Print.pptx":"Beyond_the_Hype_Cycle_Deck.pptx";
const HX=THEME.colors;
(async()=>{
const p=new pptxgen(); p.layout="LAYOUT_WIDE"; p.theme={headFontFace:"Arial",bodyFontFace:"Arial"}; p.title="Beyond the Hype Cycle"; p.author="Sushant Gaurav";
const C=p.SchemeColor, INK=C.background1, MUT=C.background2, BG=C.text1, HOT=C.accent1, COOL=C.accent2, MID=C.accent3, LINE=C.accent4;
p.defineSlideMaster({title:"TITLE",background:{color:BG},objects:[
  {placeholder:{options:{name:"title",type:"title",x:0.7,y:2.2,w:10.5,h:1.9,fontSize:54,bold:true,color:INK,align:"left",valign:"top",margin:0},text:""}},
  {placeholder:{options:{name:"body",type:"body",x:0.7,y:4.3,w:10.5,h:1.2,fontSize:20,color:MUT,align:"left",valign:"top",margin:0},text:""}}]});
p.defineSlideMaster({title:"CONTENT",background:{color:BG},slideNumber:{x:12.3,y:6.95,w:0.6,h:0.3,fontSize:10,color:MUT,align:"right"},objects:[
  {placeholder:{options:{name:"title",type:"title",x:0.7,y:0.45,w:11.9,h:1.0,fontSize:32,bold:true,color:INK,align:"left",valign:"top",margin:0},text:""}},
  {text:{text:"Beyond the Hype Cycle  |  Sushant Gaurav  |  IIMA BPGP 2025-27 Live Project",options:{x:0.7,y:6.95,w:9,h:0.3,fontSize:10,color:MUT,margin:0}}}]});
const T=(s,t,o)=>s.addText(t,Object.assign({isTextBox:true,margin:0,color:INK,fontSize:16,valign:"top"},o));
const card=(s,x,y,w,h,name)=>s.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.12,fill:{color:C.text2},line:{color:LINE,width:1},objectName:name});
const S=(title,notes)=>{const s=p.addSlide({masterName:"CONTENT",sectionTitle:SEC});s.addText(title,{placeholder:"title"});if(notes)s.addNotes(notes);return s};
let SEC="Opening"; p.addSection({title:SEC});
// 1
{const s=p.addSlide({masterName:"TITLE",sectionTitle:SEC});
 s.addShape(p.ShapeType.ellipse,{x:0.7,y:1.35,w:0.22,h:0.22,fill:{color:HOT},line:{color:HOT,width:0},objectName:"dot"});
 T(s,"Live Project  |  Area: Information Systems  |  Evidence as of 11 November 2026",{x:1.05,y:1.28,w:10,h:0.36,fontSize:14,color:MUT});
 s.addText("Beyond the Hype Cycle",{placeholder:"title"});
 s.addText("A tested index of where the story runs ahead of the proof in AI networking hardware",{placeholder:"body"});
 T(s,"Sushant Gaurav  |  IIMA BPGP 2025-27",{x:0.7,y:6.4,w:8,h:0.4,fontSize:16});
 s.addNotes("Open with the question: how do you tell an earned technology from a well-told one? This project builds and tests an instrument for that.");}
// 2
{const s=S("Three signals describe AI networking, and they disagree","Analysts track narrative maturity, equity research tracks revenue, engineers track power and cost per bit. The proposal itself mixed denominators: the 15.4 billion figure was all Ethernet switching, not data-center switching.");
 const items=[["What is said","Narrative maturity, launch claims, analyst headlines",HOT],["What is sold","Vendor revenue, market share, capital spending",MID],["What works","Power, reach, reliability, cost per bit",COOL]];
 items.forEach((it,i)=>{const x=0.7+i*4.05;card(s,x,1.75,3.8,2.5,"signal"+i);
  s.addShape(p.ShapeType.ellipse,{x:x+0.3,y:2.05,w:0.3,h:0.3,fill:{color:it[2]},line:{color:it[2],width:0},objectName:"sig-dot"+i});
  T(s,it[0],{x:x+0.3,y:2.55,w:3.2,h:0.5,fontSize:24,bold:true});T(s,it[1],{x:x+0.3,y:3.15,w:3.2,h:0.9,fontSize:15,color:MUT});});
 T(s,"The managerial question",{x:0.7,y:4.75,w:6,h:0.4,fontSize:14,color:HOT,bold:true});
 T(s,"How should a planner allocate investment across interconnect options when narrative, capital, deployable infrastructure and workload value mature at different speeds?",{x:0.7,y:5.15,w:11.6,h:1.2,fontSize:22});}
SEC="Method"; p.addSection({title:SEC});
// 3
{const s=S("Six parameters: five scores and one set of gates","Each score runs 0 to 4 on shared anchors. V is the mean of technical, adoption and economics. The gap D is claimed minus V. Capital quality is scored but kept out of the gap. Gates sit outside the arithmetic.");
 const ps=[["H","Claimed","What the narrative asserts",HOT],["T","Technical proof","Does it work at scale",COOL],["A","Adoption","Who runs it in production",COOL],["E","Buyer economics","What buyers have gained",COOL],["Q","Capital quality","How solid the money is",MID],["X","Gates","Power, packaging, memory, lasers, export rules",INK]];
 ps.forEach((it,i)=>{const x=0.7+(i%3)*4.05,y=1.7+Math.floor(i/3)*1.75;card(s,x,y,3.8,1.5,"param"+it[0]);
  T(s,it[0],{x:x+0.3,y:y+0.25,w:0.9,h:1,fontSize:44,bold:true,color:it[3]});T(s,it[1],{x:x+1.25,y:y+0.3,w:2.4,h:0.4,fontSize:18,bold:true});T(s,it[2],{x:x+1.25,y:y+0.75,w:2.4,h:0.6,fontSize:14,color:MUT});});
 T(s,[{text:"V = mean(T, A, E)      D = H − V",options:{bold:true,fontSize:24,breakLine:true}},{text:"D of +1.0 or more: story ahead.  D of −1.0 or less: proof ahead.  A blocked gate overrides any score.",options:{fontSize:15,color:MUT}}],{x:0.7,y:5.45,w:11.9,h:1.2});}
// 4
{const s=S("What is new, and how it was built","Be candid: measuring an expectation gap is not new. Kim, Kang and Hong 2026 define a Maturity-Expectation Gap from surveys. The contribution here is documented evidence with an admission rule, capital quality as its own measure, non-compensatory gates, and a tested instrument. Public and secondary data only: 152 sources logged, 71 behind the scores, 43 automated tests, 20,000 random re-scorings. On 12 November the 18 weakest evidence cells were re-checked against primary sources and two scores moved, both up. The novelty claim rests on a limited literature search.");
 const hdr=["","Claim vs proof","Graded evidence","Capital quality","Hard gates"];
 const rows=[["Gartner Hype Cycle","No","No","No","No"],["Readiness levels (TRL)","Proof only","Partly","No","No"],["Maturity-Expectation Gap (Kim et al., 2026)","By survey","No","No","No"],["This index (HVDI)","By documents","Yes","Yes","Yes"]];
 const cell=(t,o)=>({text:t,options:Object.assign({fontSize:14,color:INK,valign:"middle",fill:{color:BG},border:[{type:"none"},{type:"none"},{type:"solid",color:HX.accent4,pt:1},{type:"none"}]},o)});
 const tb=[hdr.map(h=>cell(h,{color:MUT,fontSize:12}))].concat(rows.map((r,ri)=>r.map((v,ci)=>cell(v,{bold:ri===3,color:ri===3?(ci===0?HOT:INK):(ci===0?INK:MUT)}))));
 s.addTable(tb,{x:0.7,y:1.7,w:7.6,colW:[2.75,1.55,1.15,1.1,1.05],rowH:0.68,objectName:"prior-work"});
 const st=[["10","technologies scored"],["152","public sources logged"],["43","automated tests"],["20,000","re-scorings per verdict"]];
 st.forEach((it,i)=>{const x=8.75+(i%2)*1.98,y=1.7+Math.floor(i/2)*1.72;card(s,x,y,1.87,1.6,"stat"+i);T(s,it[0],{x:x+0.18,y:y+0.2,w:1.55,h:0.7,fontSize:it[0].length>3?26:36,bold:true,color:HOT});T(s,it[1],{x:x+0.18,y:y+0.95,w:1.55,h:0.55,fontSize:12,color:MUT});});
 T(s,[{text:"Admission rule: ",options:{bold:true}},{text:"a score of 3 or more needs proof from a buyer, an independent tracker or a filing. Vendor marketing alone stops at 2."}],{x:0.7,y:5.45,w:11.9,h:0.8,fontSize:18});
 T(s,"Novelty is provisional: it rests on a limited literature search.",{x:0.7,y:6.3,w:11,h:0.4,fontSize:13,color:MUT});}
SEC="Results"; p.addSection({title:SEC});
// 6
{const s=S("Three technologies have a story ahead of their proof; only one verdict is firm","Gap by technology under equal weights. Native UALink is plus 2.00 and keeps its verdict in 99 percent of re-scorings. Ultra Ethernet transport holds at 74 percent. Ethernet scale-up, now plus 1.00 after the Meta evidence, holds at 51 percent. The other seven are directional.");
 const labs=["UALink (native)","Ultra Ethernet transport","Ethernet scale-up","Merchant DPU","Ethernet scale-out","Co-packaged optics","NVLink","InfiniBand","Linear pluggable optics","Active electrical cables"],vals=[2.00,1.33,1.00,0.67,0.67,0.67,0.33,-0.33,-0.67,-0.67];
 s.addChart(p.charts.BAR,[{name:"Gap (claimed minus evidenced)",labels:labs.slice().reverse(),values:vals.slice().reverse()}],{x:0.7,y:1.6,w:8.1,h:5.1,barDir:"bar",chartColors:[HX.accent1],invertedColors:[HX.accent2],showLegend:false,showValue:true,dataLabelPosition:"outEnd",dataLabelFormatCode:"+0.00;-0.00",dataLabelColor:HX.lt1,dataLabelFontSize:12,dataLabelFontFace:"+mn-lt",catAxisLabelColor:HX.lt1,catAxisLabelFontSize:12,catAxisLabelFontFace:"+mn-lt",valAxisLabelColor:HX.lt2,valAxisLabelFontSize:11,valAxisLabelFontFace:"+mn-lt",valAxisMinVal:-1,valAxisMaxVal:2.5,valGridLine:{color:HX.accent4,size:0.75},catGridLine:{style:"none"},barGapWidthPct:55,catAxisLabelPos:"low",objectName:"gap-chart"});
 card(s,9.2,1.8,3.4,4.6,"stability");
 T(s,"How firm",{x:9.45,y:2.0,w:2.9,h:0.4,fontSize:14,color:MUT});
 T(s,[{text:"99%",options:{fontSize:40,bold:true,color:HOT,breakLine:true}},{text:"UALink keeps its verdict",options:{fontSize:14,color:MUT,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"74%",options:{fontSize:32,bold:true,breakLine:true}},{text:"Ultra Ethernet transport (Ethernet scale-up: 51%)",options:{fontSize:14,color:MUT,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"51 to 81%",options:{fontSize:28,bold:true,breakLine:true}},{text:"the other seven: directional",options:{fontSize:14,color:MUT}}],{x:9.45,y:2.45,w:2.9,h:3.8});}
// 7
{const s=S("Where each technology sits, derived from its scores","Positions come from the study's rule, not from Gartner. Left to right is evidence building. The orange cluster at the peak is where claims run ahead. The blue cluster in the dip is where proof runs ahead of talk.");
 s.addImage({path:"deck_curve.png",x:0.7,y:1.5,w:9.6,h:9.6*1216/2264,altText:"Ten technologies placed on a hype curve by HVDI scores",objectName:"curve"});
 T(s,[{text:"Orange",options:{color:HOT,bold:true}},{text:" story ahead",options:{breakLine:true}},{text:"Grey",options:{color:MID,bold:true}},{text:" aligned",options:{breakLine:true}},{text:"Blue",options:{color:COOL,bold:true}},{text:" proof ahead of talk",options:{breakLine:true}},{text:" ",options:{breakLine:true}},{text:"Positions are this study's, not Gartner's.",options:{color:MUT,fontSize:13}}],{x:10.6,y:1.9,w:2.2,h:3,fontSize:15});}
// 8
{const s=S("Open scale-up: the first racks shipped without the fabric they were named for","AMD's first Helios racks, shipping from late Q3 2026, run scale-up over UALink-over-Ethernet on Broadcom silicon because native UALink switch chips are still in validation. That single fact explains two outlooks.");
 const cols=[["UALink, native","+2.00","Likely to stall","Simulation-based targets. Switch silicon samples at end of 2026. Venture capital only.",HOT],["Ethernet scale-up","+1.00","Likely to close","Meta says its own Ethernet scale-up switch is shipping; AMD reports first Helios racks in Q3 2026. What ships is UALink over Ethernet or a Meta variant, not ESUN.",HOT],["NVLink, incumbent","+0.33","Likely to hold","Dominates scale-up deployments. Single vendor with concentrated customers.",MID]];
 cols.forEach((c,i)=>{const x=0.7+i*4.05;card(s,x,1.75,3.8,3.9,"su"+i);T(s,c[0],{x:x+0.3,y:1.98,w:3.2,h:0.4,fontSize:18,bold:true});T(s,c[1],{x:x+0.3,y:2.5,w:3.2,h:0.95,fontSize:54,bold:true,color:c[4]});T(s,c[2],{x:x+0.3,y:3.55,w:3.2,h:0.4,fontSize:16,bold:true});T(s,c[3],{x:x+0.3,y:4.05,w:3.2,h:1.4,fontSize:14,color:MUT});});
 T(s,"A buyer choosing racks for 2026 could not buy the native open alternative.",{x:0.7,y:6.0,w:11.9,h:0.5,fontSize:20});}
// 9
{const s=S("The revenue is real, but it rests on few payers and unproven buyer economics","Customer concentration, from filings: Credo's two largest customers were 43 and 28 percent of revenue in the quarter to 1 August 2026 (49 and 32 percent in fiscal 2026); NVIDIA's three largest direct customers were 44 percent of first-half fiscal 2027 revenue. Capex as a share of operating cash flow in Q3 2026: Amazon 182, Alphabet 122, Meta 103 percent, from a secondary compilation. No technology scores above 2 of 4 on buyer economics.");
 const ax={showLegend:false,showValue:true,dataLabelPosition:"outEnd",dataLabelFormatCode:'0"%"',dataLabelColor:HX.lt1,dataLabelFontSize:12,dataLabelFontFace:"+mn-lt",catAxisLabelColor:HX.lt1,catAxisLabelFontSize:12,catAxisLabelFontFace:"+mn-lt",valAxisLabelColor:HX.lt2,valAxisLabelFontSize:11,valAxisLabelFontFace:"+mn-lt",valGridLine:{color:HX.accent4,size:0.75},catGridLine:{style:"none"},barGapWidthPct:60,showTitle:true,titleColor:HX.lt1,titleFontSize:14,titleFontFace:"+mn-lt"};
 s.addChart(p.charts.BAR,[{name:"Top-3 share",labels:["Credo (top 2, Q1 FY27)","NVIDIA (top 3, H1 FY27)"],values:[71,44]}],Object.assign({x:0.7,y:1.6,w:4.1,h:3.9,barDir:"col",chartColors:[HX.accent3],title:"Top customers, % of revenue (10-K, 10-Q)",valAxisMinVal:0,valAxisMaxVal:100,objectName:"conc-chart"},ax));
 s.addChart(p.charts.BAR,[{name:"Capex / operating cash flow",labels:["Amazon","Alphabet","Meta"],values:[182,122,103]}],Object.assign({x:5.0,y:1.6,w:4.1,h:3.9,barDir:"col",chartColors:[HX.accent1],title:"Capex, % of operating cash flow, Q3 2026",valAxisMinVal:0,valAxisMaxVal:200,objectName:"capex-chart"},ax));
 card(s,9.4,1.8,3.2,3.6,"econ");T(s,[{text:"0 of 10",options:{fontSize:44,bold:true,color:HOT,breakLine:true}},{text:"technologies score above 2 of 4 on buyer economics",options:{fontSize:15,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"The proof exists, but buyers hold it.",options:{fontSize:14,color:MUT}}],{x:9.65,y:2.05,w:2.7,h:3.2});
 T(s,"Only Ethernet scale-out reaches capital-quality level 3: Arista reports about $8.6B owed by buyers.",{x:0.7,y:5.8,w:11.9,h:0.6,fontSize:16,color:MUT});}
// 10
{const s=S("Stress test: an indium halt blocks optics, not copper","All five gates are constraining today and none is blocked. The scenarios test exposure, not likelihood. Halting indium exports blocks the four optical technologies; the six copper or protocol technologies are untouched. A Taiwan packaging disruption, tighter export rules or worse grid delays block all ten.");
 {const G=[["Ethernet scale-out",2],["InfiniBand",2],["Co-packaged optics",2],["Linear pluggable optics",2],["Ultra Ethernet transport",0],["NVLink",0],["UALink (native)",0],["Ethernet scale-up",0],["Merchant DPU",0],["Active electrical cables",0]];
  const gc=(t,o)=>({text:t,options:Object.assign({fontSize:12,color:MUT,valign:"middle",align:"center",fill:{color:BG},border:[{type:"none"},{type:"none"},{type:"solid",color:HX.accent4,pt:1},{type:"none"}]},o)});
  const head=["","Power","Packaging","Memory","Lasers","Export","Outcome"].map((h,i)=>gc(h,{fontSize:11,align:i?"center":"left"}));
  const body=G.map(g=>[gc(g[0],{align:"left",color:INK,bold:g[1]===2}),gc("Slowing"),gc("Slowing"),gc("Slowing"),g[1]===2?gc("BLOCKED",{color:HOT,bold:true}):gc("n/a",{fontSize:11}),gc("Slowing"),g[1]===2?gc("Blocked",{color:HOT,bold:true}):gc("Clear",{color:INK})]);
  s.addTable([head].concat(body),{x:0.7,y:1.55,w:8.4,colW:[2.5,0.9,1.0,0.9,1.1,0.9,1.1],rowH:0.37,objectName:"gate-matrix"});}
 card(s,9.4,1.6,3.2,4.9,"gates-take");
 T(s,[{text:"Today",options:{color:MUT,fontSize:13,breakLine:true}},{text:"5 gates constraining, 0 blocked",options:{bold:true,fontSize:18,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"Indium halt",options:{color:MUT,fontSize:13,breakLine:true}},{text:"4 optical blocked, 6 others clear",options:{bold:true,fontSize:18,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"Taiwan, export or grid shock",options:{color:MUT,fontSize:13,breakLine:true}},{text:"All 10 blocked",options:{bold:true,fontSize:18,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"Exposure tests, not predictions.",options:{color:MUT,fontSize:13}}],{x:9.65,y:1.85,w:2.7,h:4.4});
 T(s,"Interconnect readiness is not what limits value in late 2026. Delivered capacity, packaging, memory and lasers are.",{x:0.7,y:5.75,w:8.4,h:0.9,fontSize:17});}
// 11
{const s=S("Energy per bit depends on where you draw the box","Vendor-rated figures. Switch energy per bit fell about 4.7 times over four Tomahawk generations at typical load without optics. The same Tomahawk 5 switch reads 12.5 with copper and 43.3 at full load with optics. Sixty-four retimed modules explain 1,024 of the 1,578 watt difference.");
 s.addChart(p.charts.BAR,[{name:"pJ/bit",labels:["Tomahawk","Tomahawk 3","Tomahawk 4","Tomahawk 5","Tomahawk 5 with optics, full load"],values:[58.4,30.3,20.6,12.5,43.3]}],{x:0.7,y:1.6,w:7.9,h:4.9,barDir:"col",chartColors:[HX.accent3],showLegend:false,showValue:true,dataLabelPosition:"outEnd",dataLabelFormatCode:"0.0",dataLabelColor:HX.lt1,dataLabelFontSize:12,dataLabelFontFace:"+mn-lt",catAxisLabelColor:HX.lt1,catAxisLabelFontSize:12,catAxisLabelFontFace:"+mn-lt",valAxisLabelColor:HX.lt2,valAxisLabelFontSize:11,valAxisLabelFontFace:"+mn-lt",valAxisMinVal:0,valAxisMaxVal:70,valGridLine:{color:HX.accent4,size:0.75},catGridLine:{style:"none"},barGapWidthPct:60,showTitle:true,title:"Rated switch-system energy, picojoules per bit",titleColor:HX.lt1,titleFontSize:14,titleFontFace:"+mn-lt",objectName:"energy-chart"});
 card(s,9.0,1.8,3.6,4.5,"energy-take");
 T(s,[{text:"3.5x",options:{fontSize:48,bold:true,color:HOT,breakLine:true}},{text:"same switch, two boundaries: 12.5 and 43.3",options:{fontSize:14,color:MUT,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"10.6 vs 18.8 to 20.0",options:{fontSize:22,bold:true,breakLine:true}},{text:"linear against retimed 800G modules",options:{fontSize:14,color:MUT,breakLine:true}},{text:" ",options:{fontSize:8,breakLine:true}},{text:"Vendor-rated, not measured in operation.",options:{fontSize:13,color:MUT}}],{x:9.25,y:2.05,w:3.1,h:4.0});}
SEC="Implications"; p.addSection({title:SEC});
// 11
{const s=S("What a planner should do","Five postures by verdict and outlook. Each states the evidence that would move a technology up. The practice that matters most: buy the missing proof by writing matched-baseline measurement into the contract.");
 const rows=[["Deploy","Ethernet scale-out, NVLink, InfiniBand, LPO, AEC","Supply assurance; matched-baseline economics in the contract"],["Pilot at scale","Co-packaged optics","Reliability data for the generation being bought"],["Hold an option","Ethernet scale-up, Ultra Ethernet transport","No commissioning date tied to it"],["Defer","Native UALink","Switch silicon sampled, then multi-vendor interoperability"],["Prove the baseline","Merchant DPU","Host-only comparison on the buyer's own workload"]];
 const cell=(t,o)=>({text:t,options:Object.assign({fontSize:16,color:INK,valign:"middle",fill:{color:BG},border:[{type:"none"},{type:"none"},{type:"solid",color:HX.accent4,pt:1},{type:"none"}]},o)});
 const tb=[["Posture","Technologies today","Require first"].map(h=>cell(h,{color:MUT,fontSize:13}))].concat(rows.map(r=>[cell(r[0],{bold:true,color:HOT}),cell(r[1]),cell(r[2],{color:MUT})]));
 s.addTable(tb,{x:0.7,y:1.6,w:11.9,colW:[2.4,4.5,5.0],rowH:0.68,objectName:"postures"});
 T(s,"Buy the missing proof: write matched-baseline measurement into the contract.",{x:0.7,y:5.95,w:11.9,h:0.6,fontSize:20});}
// 12
{const s=S("Limits, next steps and where the evidence lives","Be direct about limits: one coder, one date, uncalibrated outlook. The back-test on earlier networking bets is the condition for calling the index predictive. Everything behind a score is in the report appendix, the source ledger and the code. Close and invite questions.");
 const cols=[["Limits",["One coder scored every cell","One date: cannot show a gap closing","Outlook rule is uncalibrated","Buyer economics is mostly private"]],["Next",["Second coder with an agreement statistic","Quarterly panel","Back-test on 400G, SDN and SmartNICs"]],["Evidence",["Report: scoring rationale and 70 references","Ledger: 152 sources, S01 to S152","Code: engine, dataset, 43 tests","Interactive page: shown live"]]];
 cols.forEach((c,i)=>{const x=0.7+i*4.05;card(s,x,1.6,3.8,3.5,"close"+i);T(s,c[0],{x:x+0.3,y:1.82,w:3.2,h:0.4,fontSize:20,bold:true,color:i===0?HOT:INK});
  T(s,c[1].map((t,k)=>({text:t,options:{bullet:true,breakLine:k<c[1].length-1}})),{x:x+0.3,y:2.4,w:3.25,h:2.5,fontSize:15,color:MUT,paraSpaceAfter:6});});
 T(s,"Key references: Kim et al. (2026); Dedehayir & Steinert (2016); Adner & Kapoor (2010); Hevner et al. (2004). Full list in the report.",{x:0.7,y:5.35,w:11.9,h:0.4,fontSize:12,color:MUT});
 T(s,"Thank you. Questions?",{x:0.7,y:5.9,w:11.9,h:0.7,fontSize:28,bold:true});}
await p.writeFile({fileName:OUT}); await applyTheme(OUT,THEME); console.log("ok");
})().catch(e=>{console.error(e);process.exit(1)});
