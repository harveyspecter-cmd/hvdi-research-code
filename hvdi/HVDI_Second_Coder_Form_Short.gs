/**
 * HVDI second coder, short form (30 statements, one click each).
 * Run: script.google.com > New project > paste > choose buildHvdiShortForm > Run > allow access > View > Logs.
 * Send ONLY the published link. Keep the edit link and the responses sheet private.
 */
const ITEMS = [
 {
  "code": "S01",
  "title": "1. Statement: “[Ultra Ethernet is] an emerging standard”",
  "help": "Ultra Ethernet: a new open standard for AI networks"
 },
 {
  "code": "S02",
  "title": "2. Statement: “[The first UALink switches are] eyeing the fourth quarter of 2026”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S03",
  "title": "3. Statement: “the inevitable momentum of NVLink as the dominant fabric in AI data centers”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S04",
  "title": "4. Statement: “SemiAnalysis calls NPO the interim step between pluggable transceivers and true CPO. [NPO = near-packaged optics]”",
  "help": "Co-packaged optics: optical links built into the chip package"
 },
 {
  "code": "S05",
  "title": "5. Statement: “Meta LPO Production Results: Link Interruptions Cut by Half”",
  "help": "Linear pluggable optics: simpler, lower-power optical modules"
 },
 {
  "code": "S06",
  "title": "6. Statement: “[NVLink is] way ahead of the open alternatives on connectivity”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S07",
  "title": "7. Statement: “Ethernet is projected to dominate both the scale-up and scale-out segments”",
  "help": "Ethernet scale-up: Ethernet used to link AI chips inside a rack"
 },
 {
  "code": "S08",
  "title": "8. Statement: “marking the official transition of co-packaged optics (CPO) into the mass production phase.”",
  "help": "Co-packaged optics: optical links built into the chip package"
 },
 {
  "code": "S09",
  "title": "9. Statement: “We're now in our third generation of NVLink-72 rack-scale systems.”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S10",
  "title": "10. Statement: “[Products using] the emerging UALink protocol are gaining traction”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S11",
  "title": "11. Statement: “[These active electrical cables] are currently sampling to customers”",
  "help": "Active electrical cables: copper cables with chips inside"
 },
 {
  "code": "S12",
  "title": "12. Statement: “Production shipments of Vera Rubin are set to begin starting this fall. [Vera Rubin = NVIDIA's NVLink rack systems]”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S13",
  "title": "13. Statement: “[AMD's networking uses] standards-based Ethernet aligned with the Ultra Ethernet Consortium for scale-out”",
  "help": "Ultra Ethernet: a new open standard for AI networks"
 },
 {
  "code": "S14",
  "title": "14. Statement: “[UALink] still needs to be broadly deployed across a hyperscale cloud”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S15",
  "title": "15. Statement: “[UALink was] a premature launch”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S16",
  "title": "16. Statement: “the vast majority of the world's data centers will just be Vera Rubin NVLink-72”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S17",
  "title": "17. Statement: “NVLink Fusion turns into soft ecosystem lock-in”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S18",
  "title": "18. Statement: “Purpose-built UALink switches capable of competing with Nvidia's NVSwitch simply aren't ready yet.”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S19",
  "title": "19. Statement: “The guidance became simple: InfiniBand for training, Spectrum‑X Ethernet for inference.”",
  "help": "InfiniBand: a network for AI clusters, mostly sold by NVIDIA"
 },
 {
  "code": "S20",
  "title": "20. Statement: “Production shipments of Vera Rubin are set to begin starting this fall. [Vera Rubin includes NVIDIA's BlueField DPU]”",
  "help": "DPU: a network card with its own processor"
 },
 {
  "code": "S21",
  "title": "21. Statement: “[NVIDIA's NVLink-based Vera Rubin platform:] with seven new chips now in full production”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S22",
  "title": "22. Statement: “With UALink products arriving in 2026, competition is heating up for scale-up interconnects”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S23",
  "title": "23. Statement: “[The consortium aims to] advance UALink technology as the open protocol for AI scale-up networking”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S24",
  "title": "24. Statement: “The Silicon One G300, G300-powered systems and optics will ship this year.”",
  "help": "Ethernet scale-out: Ethernet networks connecting AI racks"
 },
 {
  "code": "S25",
  "title": "25. Statement: “[Ethernet scale-up switches:] we're starting to see it deployed starting actually this quarter”",
  "help": "Ethernet scale-up: Ethernet used to link AI chips inside a rack"
 },
 {
  "code": "S26",
  "title": "26. Statement: “we will certainly be prepared to intercept that launch with our UALink switch”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S27",
  "title": "27. Statement: “[Analysts describe] the historical dominance of NVLink”",
  "help": "NVLink: NVIDIA's own link between AI chips"
 },
 {
  "code": "S28",
  "title": "28. Statement: “[NVIDIA's growth was] driven by strong adoption of NVLink, Spectrum-X Ethernet and InfiniBand.”",
  "help": "InfiniBand: a network for AI clusters, mostly sold by NVIDIA"
 },
 {
  "code": "S29",
  "title": "29. Statement: “[UALink:] even 1.0 solutions aren't shipping yet – they aren't due until later this year”",
  "help": "UALink: an open, multi-vendor link between AI chips"
 },
 {
  "code": "S30",
  "title": "30. Statement: “Ethernet further extended its lead in AI back-end networks, helping mitigate supply constraints.”",
  "help": "Ethernet scale-out: Ethernet networks connecting AI racks"
 }
];
const KINDS = ["Stage: what it has reached today", "Narrative: how good or big it is said to be", "Neither: it only describes features"];
const LEVELS = ["0 · Narrative only: fading, niche or losing", "1 · Stage: still being designed  |  Narrative: not ready", "2 · Stage: shipping or sampling  |  Narrative: a contender", "3 · Stage: in volume production  |  Narrative: leading", "4 · Stage: everyone's default choice  |  Narrative: the winner or the standard"];
const INTRO = "30 short statements about AI networking. For each one, answer two quick questions about what the statement SAYS (not whether it is true). About 20 minutes. No technical knowledge needed. Please do not look anything up.";
const GUIDE = "HOW TO RATE A STATEMENT\n\nQuestion 1: what is the statement about?\n• STAGE: what the product or technology has reached today.\n• NARRATIVE: how good, strong or successful people say it is, or where it is heading.\n• A prediction such as 'will become the standard' is NARRATIVE.\n\nQuestion 2: pick the level.\nSTAGE:  still being designed = 1  ·  shipping = 2  ·  in volume production = 3  ·  everyone's default = 4\nNARRATIVE:  fading or niche = 0  ·  not ready = 1  ·  a contender = 2  ·  leading = 3  ·  the winner or the standard = 4\n\nWords in [square brackets] were added only to say what the statement is about.";

function buildHvdiShortForm() {
  const form = FormApp.create('Rate 30 statements about AI networking');
  form.setDescription(INTRO).setProgressBar(true).setAllowResponseEdits(true)
      .setConfirmationMessage('Thank you, your answers are saved.');
  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addSectionHeaderItem().setTitle('How to rate').setHelpText(GUIDE);
  ITEMS.forEach(function (it, i) {
    if (i > 0 && i % 6 === 0) {
      form.addPageBreakItem().setTitle('Statements ' + (i + 1) + ' to ' + Math.min(i + 6, ITEMS.length)).setHelpText(GUIDE);
    }
    form.addMultipleChoiceItem().setTitle(it.title).setHelpText(it.help + '\n\nQuestion 1: what is the statement about?')
        .setChoiceValues(KINDS).setRequired(true);
    form.addMultipleChoiceItem().setTitle((i + 1) + '. Level')
        .setHelpText('Question 2: pick the level (skip only if you chose Neither).')
        .setChoiceValues(LEVELS);
  });
  const sheet = SpreadsheetApp.create('HVDI short form responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
  Logger.log('SEND THIS LINK: ' + form.getPublishedUrl());
  Logger.log('Edit link (private): ' + form.getEditUrl());
  Logger.log('Responses sheet (private): ' + sheet.getUrl());
}
