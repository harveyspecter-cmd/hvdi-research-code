/**
 * HVDI second coder, short form (30 statements, one click each).
 * Run: script.google.com > New project > paste > choose buildHvdiShortForm > Run > allow access > View > Logs.
 * Send ONLY the published link. Keep the edit link and the responses sheet private.
 */
const ITEMS = [
 {
  "code": "S01",
  "title": "1. “an emerging standard”",
  "help": "Ultra Ethernet transport  ·  2026-04-22  ·  Futuriom (M. Jander)\nhttps://www.futuriom.com/articles/news/top-trends-in-networking-for-ai-connectivity-from-ai-clusters-to-the-edge/2026/04"
 },
 {
  "code": "S02",
  "title": "2. “eyeing the fourth quarter of 2026”",
  "help": "UALink (native)  ·  2025-12-02  ·  Upscale AI (A. Srikumar, VP Product and Marketing),\nhttps://www.hpcwire.com/2025/12/02/upscale-ai-eyes-late-2026-for-scale-up-ualink-switch/"
 },
 {
  "code": "S03",
  "title": "3. “the inevitable momentum of NVLink as the dominant fabric in AI data centers”",
  "help": "NVLink  ·  2026-04-02  ·  Futurum Group (B. Burke)\nhttps://futurumgroup.com/?p=88414"
 },
 {
  "code": "S04",
  "title": "4. “SemiAnalysis calls NPO the interim step between pluggable transceivers and true CPO.”",
  "help": "Co-packaged optics  ·  2026-08-13  ·  SemiAnalysis, relayed by L. James (Tom's Hardware)\nhttps://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains"
 },
 {
  "code": "S05",
  "title": "5. “Meta LPO Production Results: Link Interruptions Cut by Half”",
  "help": "Linear pluggable optics  ·  2026-10-17  ·  Meta (A. Yekani, Q. Wang), OCP Global Summit 2026\nhttps://www.opencompute.org/?p=245678"
 },
 {
  "code": "S06",
  "title": "6. “way ahead of the open alternatives on connectivity”",
  "help": "NVLink  ·  2026-04-07  ·  David Harold, Jon Peddie Research,\nhttps://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html"
 },
 {
  "code": "S07",
  "title": "7. “Ethernet is projected to dominate both the scale-up and scale-out segments”",
  "help": "Ethernet scale-up  ·  2026-02-04  ·  Dell'Oro Group\nhttps://www.delloro.com/news/ai-back-end-switch-market-will-push-past-100-billion-by-2030/"
 },
 {
  "code": "S08",
  "title": "8. “marking the official transition of co-packaged optics (CPO) into the mass production phase.”",
  "help": "Co-packaged optics  ·  2026-07-27  ·  TrendForce\nhttps://www.trendforce.com/presscenter/news/20260727-13151.html"
 },
 {
  "code": "S09",
  "title": "9. “We're now in our third generation of NVLink-72 rack-scale systems.”",
  "help": "NVLink  ·  2026-08-26  ·  NVIDIA (J. Huang, CEO; C. Kress, CFO), Q2 FY2027 earnings call\nhttps://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "S10",
  "title": "10. “the emerging UALink protocol are gaining traction”",
  "help": "UALink (native)  ·  2026-05-05  ·  The Register (T. Mann)\nhttps://www.theregister.com/2026/05/05/nvlink_astera_big_swich/"
 },
 {
  "code": "S11",
  "title": "11. “are currently sampling to customers”",
  "help": "Active electrical cables  ·  2026-10-13  ·  Marvell\nhttps://investor.marvell.com/news-events/press-releases/detail/1039/marvell-bolsters-connectivity-portfolio-with-new-3-2t-protocol-aware-retimer-and-second-generation-1-6t-aec-dsp"
 },
 {
  "code": "S12",
  "title": "12. “Production shipments of Vera Rubin are set to begin starting this fall.”",
  "help": "NVLink  ·  2026-05-31  ·  NVIDIA\nhttps://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory"
 },
 {
  "code": "S13",
  "title": "13. “standards-based Ethernet aligned with the Ultra Ethernet Consortium for scale-out”",
  "help": "Ultra Ethernet transport  ·  2026-07-23  ·  AMD\nhttps://newsroom.amd.com/news/aai-2026-helios-update/"
 },
 {
  "code": "S14",
  "title": "14. “still needs to be broadly deployed across a hyperscale cloud”",
  "help": "UALink (native)  ·  2026-03-23  ·  Futurum Group (B. Burke)\nhttps://futurumgroup.com/insights/marvells-xconn-buy-yields-a-two-pronged-open-fabric-play-against-nvlink/"
 },
 {
  "code": "S15",
  "title": "15. “a premature launch”",
  "help": "UALink (native)  ·  2026-04-07  ·  Network World (M. Cooter)\nhttps://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html"
 },
 {
  "code": "S16",
  "title": "16. “the vast majority of the world's data centers will just be Vera Rubin NVLink-72”",
  "help": "NVLink  ·  2026-08-26  ·  NVIDIA (J. Huang, CEO), Q2 FY2027 earnings call\nhttps://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "S17",
  "title": "17. “NVLink Fusion turns into soft ecosystem lock-in”",
  "help": "NVLink  ·  2026-04-02  ·  Tom's Hardware (L. James)\nhttps://www.tomshardware.com/tech-industry/nvidia-invests-2-billion-in-marvell-whose-biggest-clients-are-trying-to-replace-nvidia-chips"
 },
 {
  "code": "S18",
  "title": "18. “Purpose-built UALink switches capable of competing with Nvidia's NVSwitch simply aren't ready yet.”",
  "help": "UALink (native)  ·  2026-01-22  ·  The Register (T. Mann)\nhttps://www.theregister.com/2026/01/22/upscale_skyhammer_nvidia/"
 },
 {
  "code": "S19",
  "title": "19. “The guidance became simple: InfiniBand for training, Spectrum‑X Ethernet for inference.”",
  "help": "InfiniBand  ·  2026-03-20  ·  NAND Research (M. McDowell)\nhttps://nand-research.com/nvidiagtc-2026-networking/"
 },
 {
  "code": "S20",
  "title": "20. “Production shipments of Vera Rubin are set to begin starting this fall.”",
  "help": "Merchant DPU  ·  2026-05-31  ·  NVIDIA\nhttps://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory"
 },
 {
  "code": "S21",
  "title": "21. “with seven new chips now in full production”",
  "help": "NVLink  ·  2026-03-16  ·  NVIDIA (GTC 2026 press release)\nhttps://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/"
 },
 {
  "code": "S22",
  "title": "22. “With UALink products arriving in 2026, competition is heating up for scale-up interconnects”",
  "help": "UALink (native)  ·  2025-12-02  ·  HPCwire (A. Woodie)\nhttps://www.hpcwire.com/2025/12/02/upscale-ai-eyes-late-2026-for-scale-up-ualink-switch/"
 },
 {
  "code": "S23",
  "title": "23. “advance UALink technology as the open protocol for AI scale-up networking”",
  "help": "UALink (native)  ·  2026-05-06  ·  UALink Consortium blog (N. Morgan)\nhttps://ualinkconsortium.org/blog/ualink-consortium-highlights-open-scale-up-innovation-at-xcelerated-compute-1448/"
 },
 {
  "code": "S24",
  "title": "24. “The Silicon One G300, G300-powered systems and optics will ship this year.”",
  "help": "Ethernet scale-out  ·  2026-02-10  ·  Cisco\nhttps://investor.cisco.com/news/news-details/2026/Cisco-Announces-New-Silicon-One-G300-Advanced-Systems-and-Optics-to-Power-and-Scale-AI-Data-Centers-for-the-Agentic-Era/default.aspx"
 },
 {
  "code": "S25",
  "title": "25. “we're starting to see it deployed starting actually this quarter”",
  "help": "Ethernet scale-up  ·  2026-09-02  ·  Broadcom (C. Kawwas), Q3 FY2026 earnings call\nhttps://www.webull.com/news/15511095937917952"
 },
 {
  "code": "S26",
  "title": "26. “we will certainly be prepared to intercept that launch with our UALink switch”",
  "help": "UALink (native)  ·  2026-05-05  ·  Astera Labs (J. Mohan, CEO), Q1 2026 earnings call\nhttps://www.fool.com/earnings/call-transcripts/2026/05/05/astera-labs-alab-q1-2026-earnings-transcript/"
 },
 {
  "code": "S27",
  "title": "27. “the historical dominance of NVLink”",
  "help": "NVLink  ·  2026-03-23  ·  Futurum Group (B. Burke)\nhttps://futurumgroup.com/insights/marvells-xconn-buy-yields-a-two-pronged-open-fabric-play-against-nvlink/"
 },
 {
  "code": "S28",
  "title": "28. “driven by strong adoption of NVLink, Spectrum-X Ethernet and InfiniBand.”",
  "help": "InfiniBand  ·  2026-02-25  ·  NVIDIA (C. Kress, CFO), Q4 FY2026 earnings call\nhttps://s201.q4cdn.com/141608511/files/doc_financials/2026/q4/NVDA-Q4-2026-Earnings-Call-25-February-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "S29",
  "title": "29. “even 1.0 solutions aren't shipping yet – they aren't due until later this year”",
  "help": "UALink (native)  ·  2026-04-07  ·  David Harold, Jon Peddie Research,\nhttps://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html"
 },
 {
  "code": "S30",
  "title": "30. “Ethernet further extended its lead in AI back-end networks, helping mitigate supply constraints.”",
  "help": "Ethernet scale-out  ·  2026-09-03  ·  Dell'Oro Group\nhttps://www.delloro.com/news/ai-back-end-networks-switch-sales-surpass-front-end-networks-for-the-first-time-in-2q2026/"
 }
];
const CHOICES = ["Stage 1  ·  a standard or spec is being written", "Stage 2  ·  launched, sampling or shipping", "Stage 3  ·  volume production", "Stage 4  ·  the default choice", "Narrative 0  ·  declining or niche", "Narrative 1  ·  not ready yet", "Narrative 2  ·  a contender", "Narrative 3  ·  leading", "Narrative 4  ·  the default, or the inevitable winner", "Not a claim  ·  only describes features"];
const INTRO = "30 short statements about AI networking technologies. For each, pick the ONE option that best matches what the statement SAYS, not whether it is true. About 20 minutes. No technical knowledge needed. Please work alone.";
const GUIDE = "STAGE = what it has reached now.   NARRATIVE = how strong it is, or where it is heading.\n\n• 'shipping' = Stage 2,  'volume production' = Stage 3\n• 'leading' = Narrative 3,  'the standard' or 'will inevitably win' = Narrative 4\n• 'not ready' = Narrative 1\n• a confident forecast ('will become the standard') is Narrative\n• if a statement does two things, rate its main point";

function buildHvdiShortForm() {
  const form = FormApp.create('Rate 30 statements about AI networking');
  form.setDescription(INTRO).setProgressBar(true).setAllowResponseEdits(true)
      .setConfirmationMessage('Thank you, your answers are saved.');
  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addSectionHeaderItem().setTitle('How to choose').setHelpText(GUIDE);
  ITEMS.forEach(function (it, i) {
    if (i > 0 && i % 6 === 0) {
      form.addPageBreakItem().setTitle('Statements ' + (i + 1) + ' to ' + Math.min(i + 6, ITEMS.length)).setHelpText(GUIDE);
    }
    form.addMultipleChoiceItem().setTitle(it.title).setHelpText(it.help)
        .setChoiceValues(CHOICES).setRequired(true);
  });
  const sheet = SpreadsheetApp.create('HVDI short form responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
  Logger.log('SEND THIS LINK: ' + form.getPublishedUrl());
  Logger.log('Edit link (private): ' + form.getEditUrl());
  Logger.log('Responses sheet (private): ' + sheet.getUrl());
}
