/**
 * HVDI blind second-coder questionnaire. Builds a Google Form with 76 statements.
 * How to run: script.google.com > New project > paste this file > select buildHvdiCoderForm > Run > allow access.
 * The log prints the form's edit link and the link to send to the coder. Responses go to a linked Google Sheet.
 * Do not share the edit link, the response sheet or the answer key with the coder.
 */
const CLAIMS = [
 {
  "code": "C01",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-03-23\nWho said it: Futurum Group (B. Burke) (originating analyst)\n\nQuote: “still needs to be broadly deployed across a hyperscale cloud”\n\nLink: https://futurumgroup.com/insights/marvells-xconn-buy-yields-a-two-pronged-open-fabric-play-against-nvlink/"
 },
 {
  "code": "C02",
  "text": "Technology: Linear pluggable optics (LPO)\nDate: 2026-10-17\nWho said it: Meta (A. Yekani, Q. Wang), OCP Global Summit 2026 (hyperscale buyer/operator)\n\nQuote: “Meta LPO Production Results: Link Interruptions Cut by Half”\n\nLink: https://www.opencompute.org/?p=245678"
 },
 {
  "code": "C03",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-03-10\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Although InfiniBand continues to grow, Ethernet is expanding at a much faster pace.”\n\nLink: https://www.delloro.com/news/ethernet-more-than-doubles-size-of-infiniband-as-the-leading-fabric-for-ai-scale-out-networks-in-2025/"
 },
 {
  "code": "C04",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-10-19\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “These are distinct architectures and development stages”\n\nLink: https://www.delloro.com/ocp-2026-optics-takes-center-stage-in-enabling-the-next-wave-of-ai-networking-and-high-speed-switching/"
 },
 {
  "code": "C05",
  "text": "Technology: Linear pluggable optics (LPO)\nDate: 2026-10-18\nWho said it: Linktel Technologies (vendor)\n\nQuote: “volume production already in place”\n\nLink: https://vir.com.vn/linktel-technologies-displays-16t-optical-transceivers-at-ocp-summit-2026-163142.html"
 },
 {
  "code": "C06",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-04-07\nWho said it: David Harold, Jon Peddie Research, via Network World (originating analyst)\n\nQuote: “way ahead of the open alternatives on connectivity”\n\nLink: https://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html"
 },
 {
  "code": "C07",
  "text": "Technology: Active electrical cables (AEC)\nDate: 2025-12-09\nWho said it: 650 Group (A. Weckel), quoted in Marvell release (originating analyst)\n\nQuote: “AECs are emerging as one of the fastest-growing segments in scale-up and scale-out interconnects”\n\nLink: https://www.businesswire.com/news/home/20251209603264/en"
 },
 {
  "code": "C08",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-03-10\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Although InfiniBand continues to grow, Ethernet is expanding at a much faster pace.”\n\nLink: https://www.delloro.com/news/ethernet-more-than-doubles-size-of-infiniband-as-the-leading-fabric-for-ai-scale-out-networks-in-2025/"
 },
 {
  "code": "C09",
  "text": "Technology: Merchant DPU / SmartNIC\nDate: 2026-07-23\nWho said it: AMD (vendor)\n\nQuote: “the default networking of choice for the AMD Helios™ rack-scale solution”\n\nLink: https://www.amd.com/en/blogs/2026/amd-pensando-vulcano-800-ai-nic-scale-out-and-across.html"
 },
 {
  "code": "C10",
  "text": "Technology: Merchant DPU / SmartNIC\nDate: 2026-05-31\nWho said it: NVIDIA (vendor)\n\nQuote: “Production shipments of Vera Rubin are set to begin starting this fall.”\n\nLink: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory"
 },
 {
  "code": "C11",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-02-04\nWho said it: Dell'Oro Group (originating analyst)\n\nQuote: “Ethernet is projected to dominate both the scale-up and scale-out segments”\n\nLink: https://www.delloro.com/news/ai-back-end-switch-market-will-push-past-100-billion-by-2030/"
 },
 {
  "code": "C12",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-08-26\nWho said it: NVIDIA (J. Huang, CEO), Q2 FY2027 earnings call (vendor)\n\nQuote: “the vast majority of the world's data centers will just be Vera Rubin NVLink-72”\n\nLink: https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "C13",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-04-07\nWho said it: Network World (M. Cooter) (trade press)\n\nQuote: “a premature launch”\n\nLink: https://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html"
 },
 {
  "code": "C14",
  "text": "Technology: Active electrical cables (AEC)\nDate: 2026-04-11\nWho said it: Vijay Rakesh, Mizuho, via MarketWatch (B. Nguyen) (sell-side analyst)\n\nQuote: “will maintain their dominant market share in short-reach AI interconnect”\n\nLink: https://www.itiger.com/news/2626252541"
 },
 {
  "code": "C15",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-01-09\nWho said it: Jayshree Ullal, Arista CEO, via ICC (itiger) (vendor)\n\nQuote: “以太网始终是最终的赢家和均衡器”\nEnglish gist: Ethernet is always the eventual winner and equaliser.\n\nLink: https://www.itiger.com/news/2602310929"
 },
 {
  "code": "C16",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2025-12-17\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Ethernet surpassed InfiniBand in market adoption.”\n\nLink: https://www.delloro.com/2026-predictions-data-center-switch-frontend-ai-backed-networks/"
 },
 {
  "code": "C17",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2025-12-02\nWho said it: HPCwire (A. Woodie) (trade press)\n\nQuote: “With UALink products arriving in 2026, competition is heating up for scale-up interconnects”\n\nLink: https://www.hpcwire.com/2025/12/02/upscale-ai-eyes-late-2026-for-scale-up-ualink-switch/"
 },
 {
  "code": "C18",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-10-07\nWho said it: Arista (vendor)\n\nQuote: “Arista is introducing Etherlink SU-144.”\n\nLink: https://www.arista.com/en/company/news/press-release/24818-pr-20261007"
 },
 {
  "code": "C19",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-04-02\nWho said it: Tom's Hardware (L. James) (trade press)\n\nQuote: “NVLink Fusion turns into soft ecosystem lock-in”\n\nLink: https://www.tomshardware.com/tech-industry/nvidia-invests-2-billion-in-marvell-whose-biggest-clients-are-trying-to-replace-nvidia-chips"
 },
 {
  "code": "C20",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-10-19\nWho said it: 451 Research, S&P Global (M. Fratto) (originating analyst)\n\nQuote: “the industry is transitioning to high-speed, lossless Ethernet fabrics”\n\nLink: https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/ai-networking-competition-moves-beyond-bandwidth-to-openness-and-efficiency"
 },
 {
  "code": "C21",
  "text": "Technology: Co-packaged optics (CPO)\nDate: 2026-08-13\nWho said it: SemiAnalysis, relayed by L. James (Tom's Hardware) (analyst)\n\nQuote: “SemiAnalysis calls NPO the interim step between pluggable transceivers and true CPO.”\n\nLink: https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains"
 },
 {
  "code": "C22",
  "text": "Technology: Ultra Ethernet transport (UEC)\nDate: 2026-10-14\nWho said it: Tom Emmons, Chair, UEC Technical Advisory Committee, via Network World (consortium/promoter)\n\nQuote: “dotting the i's and crossing the t's to enable companies to build UEC NICs”\n\nLink: https://www.networkworld.com/article/4235340/ultra-ethernet-1-1-extends-the-specification-to-scale-up-networks-and-adds-programmable-congestion-control.html"
 },
 {
  "code": "C23",
  "text": "Technology: Ultra Ethernet transport (UEC)\nDate: 2026-07-23\nWho said it: AMD (vendor)\n\nQuote: “standards-based Ethernet aligned with the Ultra Ethernet Consortium for scale-out”\n\nLink: https://newsroom.amd.com/news/aai-2026-helios-update/"
 },
 {
  "code": "C24",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-09-07\nWho said it: BUSINESS NETWORK (坪田弘樹, editorial) (trade press)\n\nQuote: “NVLink対抗の新標準「ESUN」とは”\nEnglish gist: What is ESUN, the new standard competing with NVLink? (headline)\n\nLink: https://businessnetwork.jp/article/36271/"
 },
 {
  "code": "C25",
  "text": "Technology: Active electrical cables (AEC)\nDate: 2026-03-02\nWho said it: Credo (W. Brennan, CEO; D. Fleming, CFO), Q3 FY2026 call, via MarketBeat (vendor)\n\nQuote: “substantial year-over-year growth across 4 domestic hyperscale customers”\n\nLink: https://finance.yahoo.com/news/credo-technology-group-q3-earnings-232723083.html"
 },
 {
  "code": "C26",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-03-16\nWho said it: NVIDIA (GTC 2026 press release) (vendor)\n\nQuote: “with seven new chips now in full production”\n\nLink: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/"
 },
 {
  "code": "C27",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-04-02\nWho said it: Futurum Group (B. Burke) (originating analyst)\n\nQuote: “the inevitable momentum of NVLink as the dominant fabric in AI data centers”\n\nLink: https://futurumgroup.com/?p=88414"
 },
 {
  "code": "C28",
  "text": "Technology: Active electrical cables (AEC)\nDate: 2026-07-10\nWho said it: CRU Group (E. Balla) (analyst (commodities))\n\nQuote: “progressively narrowing the space in which copper remains the natural choice”\n\nLink: https://www.crugroup.com/en/communities/thought-leadership/2026/the-outlook-of-copper-based-data-cables-in-ai-data-centres/"
 },
 {
  "code": "C29",
  "text": "Technology: Co-packaged optics (CPO)\nDate: 2026-07-27\nWho said it: TrendForce (originating analyst)\n\nQuote: “marking the official transition of co-packaged optics (CPO) into the mass production phase.”\n\nLink: https://www.trendforce.com/presscenter/news/20260727-13151.html"
 },
 {
  "code": "C30",
  "text": "Technology: Active electrical cables (AEC)\nDate: 2026-10-13\nWho said it: Marvell (vendor)\n\nQuote: “are currently sampling to customers”\n\nLink: https://investor.marvell.com/news-events/press-releases/detail/1039/marvell-bolsters-connectivity-portfolio-with-new-3-2t-protocol-aware-retimer-and-second-generation-1-6t-aec-dsp"
 },
 {
  "code": "C31",
  "text": "Technology: Ultra Ethernet transport (UEC)\nDate: 2026-10-12\nWho said it: Meta (R. Sunkad, O. Baldonado, Engineering at Meta) (hyperscale buyer)\n\nQuote: (no single quote)\nNo single quote. Open the link: what does Meta say about Ultra Ethernet (UEC) transport?\n\nLink: https://engineering.fb.com/2026/10/12/open-source/ocp-summit-2026-powering-ai-with-open-innovations-in-scale-up-scale-out-and-scale-across-networks/"
 },
 {
  "code": "C32",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-02-25\nWho said it: NVIDIA (C. Kress, CFO), Q4 FY2026 earnings call (vendor)\n\nQuote: “driven by strong adoption of NVLink, Spectrum-X Ethernet and InfiniBand.”\n\nLink: https://s201.q4cdn.com/141608511/files/doc_financials/2026/q4/NVDA-Q4-2026-Earnings-Call-25-February-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "C33",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-04-28\nWho said it: Futurum Group (T. Hollingsworth) (originating analyst)\n\nQuote: “InfiniBand is the dominant interconnection method for GPU networking today”\n\nLink: https://futurumgroup.com/press-release/scale-across-ai-networking-the-third-dimension-of-ai-infrastructure-design/"
 },
 {
  "code": "C34",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-10-13\nWho said it: Futurum Group (T. Hollingsworth) (originating analyst)\n\nQuote: “has taken most of the AI back end”\n\nLink: https://futurumgroup.com/wp-content/uploads/2026/10/Ethernet-Wont-Collapse-the-Four-Enterprise-Networks-Into-One_AINTH202609.pdf"
 },
 {
  "code": "C35",
  "text": "Technology: Ultra Ethernet transport (UEC)\nDate: 2026-04-22\nWho said it: Futuriom (M. Jander) (originating analyst)\n\nQuote: “an emerging standard”\n\nLink: https://www.futuriom.com/articles/news/top-trends-in-networking-for-ai-connectivity-from-ai-clusters-to-the-edge/2026/04"
 },
 {
  "code": "C36",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-01-22\nWho said it: The Register (T. Mann) (trade press)\n\nQuote: “Purpose-built UALink switches capable of competing with Nvidia's NVSwitch simply aren't ready yet.”\n\nLink: https://www.theregister.com/2026/01/22/upscale_skyhammer_nvidia/"
 },
 {
  "code": "C37",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-07-23\nWho said it: AMD (vendor)\n\nQuote: “AMD is introducing new scale-up networking capabilities”\n\nLink: https://www.amd.com/en/blogs/2026/amd-helios-resilient-scale-up-networking-for-ai.html"
 },
 {
  "code": "C38",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-08-26\nWho said it: NVIDIA (C. Kress, CFO), Q2 FY2027 earnings call (vendor)\n\nQuote: “Spectrum-X Ethernet, which grew 2.6x on a year-over-year basis”\n\nLink: https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "C39",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-11-03\nWho said it: Arista, Q3 2026 earnings release (Form 8-K Ex. 99.1) (vendor)\n\nQuote: “Arista launched open standards-based rack-scale architectures for scale-up and scale-out AI networks”\n\nLink: https://last10k.com/sec-filings/anet/0001596532-26-000252.htm"
 },
 {
  "code": "C40",
  "text": "Technology: Co-packaged optics (CPO)\nDate: 2026-03-10\nWho said it: LightCounting, via Lightwave (S. Buckley) (originating analyst)\n\nQuote: “lead to a stronger growth for the market in 2028-2031”\n\nLink: https://lightwaveonline.com/home/article/55362899/ai-scale-up-raises-the-stakes-for-transceivers-and-cpo-adoption"
 },
 {
  "code": "C41",
  "text": "Technology: Ultra Ethernet transport (UEC)\nDate: 2026-01-13\nWho said it: Le Monde Informatique (La rédaction) (trade press)\n\nQuote: “mieux rivaliser avec Infiniband”\nEnglish gist: ...to compete better with InfiniBand.\n\nLink: https://www.lemondeinformatique.fr/actualites/lire-les-consortiums-ethernet-fixent-leurs-priorites-2026-99016.html"
 },
 {
  "code": "C42",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-06-02\nWho said it: Dell'Oro Group (originating analyst)\n\nQuote: “Ethernet Extends Lead in AI Scale-Out Networks Despite Strong InfiniBand Rebound”\n\nLink: https://www.delloro.com/news/ethernet-extends-lead-in-ai-scale-out-networks-despite-strong-infiniband-rebound/"
 },
 {
  "code": "C43",
  "text": "Technology: Active electrical cables (AEC)\nDate: 2025-12-01\nWho said it: Credo (W. Brennan, CEO) (vendor)\n\nQuote: “continued growth in our core AEC and IC franchises”\n\nLink: https://www.businesswire.com/news/home/20251201598056/en"
 },
 {
  "code": "C44",
  "text": "Technology: Ultra Ethernet transport (UEC)\nDate: 2026-10-07\nWho said it: Arista (vendor)\n\nQuote: (no single quote)\nNo single quote. Open the link: what does Arista say about Ultra Ethernet (UEC) transport?\n\nLink: https://www.arista.com/en/company/news/press-release/24818-pr-20261007"
 },
 {
  "code": "C45",
  "text": "Technology: Co-packaged optics (CPO)\nDate: 2026-03-05\nWho said it: Lawrence Gasman, CIR (by-lined in Lightwave) (originating analyst)\n\nQuote: “CPO becomes the only technology to date that can do the job.”\n\nLink: https://www.lightwaveonline.com/home/article/55362126/co-packaged-optics-and-the-ai-data-center-from-skepticism-to-strategic-adoption"
 },
 {
  "code": "C46",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2025-11-17\nWho said it: NVIDIA (S. Martin, NVIDIA Blog) (vendor)\n\nQuote: “continues to be widely adopted to meet the demands of massive-scale AI”\n\nLink: https://blogs.nvidia.com/?p=87393"
 },
 {
  "code": "C47",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-06-17\nWho said it: IDC (Nicholson, Butler, Jirovsky, Anesini) (originating analyst)\n\nQuote: “has emerged as the preferred network interconnect for large-scale AI training”\n\nLink: https://www.idc.com/resource-center/blog/nvidia-becomes-1-in-datacenter-ethernet-switching-as-1q26-market-surges-39-8-to-15-4-billion/"
 },
 {
  "code": "C48",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-03-12\nWho said it: Broadcom (vendor)\n\nQuote: “Tomahawk 6 moved rapidly from initial samples to production deployment.”\n\nLink: https://investors.broadcom.com/news-releases/news-release-details/broadcom-now-shipping-worlds-first-1024-tbps-switch-production"
 },
 {
  "code": "C49",
  "text": "Technology: Linear pluggable optics (LPO)\nDate: 2026-08-05\nWho said it: Semtech, via DataCenterNews US (M. Tarre) (vendor)\n\nQuote: “LPO is moving from an experimental concept to a design option”\n\nLink: https://datacenter.news/story/semtech-backs-linear-pluggable-optics-for-ai-data-centres"
 },
 {
  "code": "C50",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-03-23\nWho said it: Futurum Group (B. Burke) (originating analyst)\n\nQuote: “the historical dominance of NVLink”\n\nLink: https://futurumgroup.com/insights/marvells-xconn-buy-yields-a-two-pronged-open-fabric-play-against-nvlink/"
 },
 {
  "code": "C51",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-05-06\nWho said it: UALink Consortium blog (N. Morgan) (consortium/promoter)\n\nQuote: “advance UALink technology as the open protocol for AI scale-up networking”\n\nLink: https://ualinkconsortium.org/blog/ualink-consortium-highlights-open-scale-up-innovation-at-xcelerated-compute-1448/"
 },
 {
  "code": "C52",
  "text": "Technology: Merchant DPU / SmartNIC\nDate: 2026-08-12\nWho said it: Dell'Oro Group (originating analyst)\n\nQuote: “NICs will increasingly shift toward custom silicon as hyperscalers seek greater efficiency”\n\nLink: https://www.delloro.com/news/data-center-it-semiconductors-and-components-market-to-surpass-1-8-trillion-over-next-five-years/"
 },
 {
  "code": "C53",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-10-12\nWho said it: Meta (R. Sunkad, O. Baldonado, Engineering at Meta) (hyperscale buyer)\n\nQuote: “With Tahan shipping today”\n\nLink: https://engineering.fb.com/2026/10/12/open-source/ocp-summit-2026-powering-ai-with-open-innovations-in-scale-up-scale-out-and-scale-across-networks/"
 },
 {
  "code": "C54",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-05-31\nWho said it: NVIDIA (vendor)\n\nQuote: “Production shipments of Vera Rubin are set to begin starting this fall.”\n\nLink: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory"
 },
 {
  "code": "C55",
  "text": "Technology: Co-packaged optics (CPO)\nDate: 2026-10-19\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Early commercialization should not be confused with broad adoption.”\n\nLink: https://www.delloro.com/ocp-2026-optics-takes-center-stage-in-enabling-the-next-wave-of-ai-networking-and-high-speed-switching/"
 },
 {
  "code": "C56",
  "text": "Technology: Co-packaged optics (CPO)\nDate: 2026-05-31\nWho said it: NVIDIA (vendor)\n\nQuote: “co-packaged-optics (CPO)-based switches with 200Gb/s SerDes — now in production”\n\nLink: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory"
 },
 {
  "code": "C57",
  "text": "Technology: Linear pluggable optics (LPO)\nDate: 2026-03-17\nWho said it: Centera Photonics / NewPhotonics (vendor)\n\nQuote: “accelerating the LPO transition from promise to production reality”\n\nLink: https://www.prnewswire.com/il/news-releases/centera-photonics-announces-first-1-6tbps-dr8-lpo-transceiver-based-on-newphotonics-lpo-pic-with-integrated-ospic-optical-signal-processor-302713692.html"
 },
 {
  "code": "C58",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-10-19\nWho said it: 451 Research, S&P Global (M. Fratto) (originating analyst)\n\nQuote: “the industry is transitioning to high-speed, lossless Ethernet fabrics”\n\nLink: https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/ai-networking-competition-moves-beyond-bandwidth-to-openness-and-efficiency"
 },
 {
  "code": "C59",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-05-05\nWho said it: Astera Labs (J. Mohan, CEO), Q1 2026 earnings call (vendor)\n\nQuote: “we will certainly be prepared to intercept that launch with our UALink switch”\n\nLink: https://www.fool.com/earnings/call-transcripts/2026/05/05/astera-labs-alab-q1-2026-earnings-transcript/"
 },
 {
  "code": "C60",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-11-03\nWho said it: Arista (J. Ullal, CEO), Q3 2026 earnings call (vendor)\n\nQuote: “having already surpassed 100 Etherlink customers.”\n\nLink: https://www.webull.com/news/15866284470803456"
 },
 {
  "code": "C61",
  "text": "Technology: Merchant DPU / SmartNIC\nDate: 2026-01-05\nWho said it: NVIDIA (J. Huang) (vendor)\n\nQuote: “is now in full production”\n\nLink: https://blogs.nvidia.com/blog/2026-ces-special-presentation"
 },
 {
  "code": "C62",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-04-07\nWho said it: David Harold, Jon Peddie Research, via Network World (originating analyst)\n\nQuote: “even 1.0 solutions aren't shipping yet – they aren't due until later this year”\n\nLink: https://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html"
 },
 {
  "code": "C63",
  "text": "Technology: Merchant DPU / SmartNIC\nDate: 2026-07-15\nWho said it: Futuriom (M. Jander) (originating analyst)\n\nQuote: “ConnectX series SmartNICs and BlueField DPUs lead the market”\n\nLink: https://www.futuriom.com/articles/news/smartnics-and-dpus-a-market-update/2026/07"
 },
 {
  "code": "C64",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2026-09-02\nWho said it: Broadcom (C. Kawwas), Q3 FY2026 earnings call (vendor)\n\nQuote: “we're starting to see it deployed starting actually this quarter”\n\nLink: https://www.webull.com/news/15511095937917952"
 },
 {
  "code": "C65",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-03-20\nWho said it: NAND Research (M. McDowell) (originating analyst)\n\nQuote: “The guidance became simple: InfiniBand for training, Spectrum‑X Ethernet for inference.”\n\nLink: https://nand-research.com/nvidiagtc-2026-networking/"
 },
 {
  "code": "C66",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2026-05-05\nWho said it: The Register (T. Mann) (trade press)\n\nQuote: “the emerging UALink protocol are gaining traction”\n\nLink: https://www.theregister.com/2026/05/05/nvlink_astera_big_swich/"
 },
 {
  "code": "C67",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-10-12\nWho said it: Cisco (vendor)\n\nQuote: “the first G300-powered systems are currently shipping to customers.”\n\nLink: https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m10/cisco-advances-scalability-and-openness-at-ocp-2026.html"
 },
 {
  "code": "C68",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-01-09\nWho said it: Jayshree Ullal, Arista CEO, via ICC (itiger) (vendor)\n\nQuote: (no single quote)\nNo single quote. Open the link: what does Arista's CEO say about InfiniBand?\n\nLink: https://www.itiger.com/news/2602310929"
 },
 {
  "code": "C69",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-09-03\nWho said it: Dell'Oro Group (originating analyst)\n\nQuote: “Ethernet further extended its lead in AI back-end networks, helping mitigate supply constraints.”\n\nLink: https://www.delloro.com/news/ai-back-end-networks-switch-sales-surpass-front-end-networks-for-the-first-time-in-2q2026/"
 },
 {
  "code": "C70",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2025-12-17\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Ethernet surpassed InfiniBand in market adoption.”\n\nLink: https://www.delloro.com/2026-predictions-data-center-switch-frontend-ai-backed-networks/"
 },
 {
  "code": "C71",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-06-02\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Ethernet Extends Lead in AI Scale-Out Networks Despite Strong InfiniBand Rebound”\n\nLink: https://www.delloro.com/news/ethernet-extends-lead-in-ai-scale-out-networks-despite-strong-infiniband-rebound/"
 },
 {
  "code": "C72",
  "text": "Technology: Ethernet for scale-up (ESUN, SUE)\nDate: 2025-12-17\nWho said it: Dell'Oro Group (S. Boujelbene) (originating analyst)\n\nQuote: “Scale-up emerges as a new battlefield for Ethernet.”\n\nLink: https://www.delloro.com/2026-predictions-data-center-switch-frontend-ai-backed-networks/"
 },
 {
  "code": "C73",
  "text": "Technology: UALink, native (open scale-up link)\nDate: 2025-12-02\nWho said it: Upscale AI (A. Srikumar, VP Product and Marketing), via HPCwire (vendor)\n\nQuote: “eyeing the fourth quarter of 2026”\n\nLink: https://www.hpcwire.com/2025/12/02/upscale-ai-eyes-late-2026-for-scale-up-ualink-switch/"
 },
 {
  "code": "C74",
  "text": "Technology: NVLink (NVIDIA scale-up link)\nDate: 2026-08-26\nWho said it: NVIDIA (J. Huang, CEO; C. Kress, CFO), Q2 FY2027 earnings call (vendor)\n\nQuote: “We're now in our third generation of NVLink-72 rack-scale systems.”\n\nLink: https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"
 },
 {
  "code": "C75",
  "text": "Technology: Ethernet for scale-out AI networks\nDate: 2026-02-10\nWho said it: Cisco (vendor)\n\nQuote: “The Silicon One G300, G300-powered systems and optics will ship this year.”\n\nLink: https://investor.cisco.com/news/news-details/2026/Cisco-Announces-New-Silicon-One-G300-Advanced-Systems-and-Optics-to-Power-and-Scale-AI-Data-Centers-for-the-Agentic-Era/default.aspx"
 },
 {
  "code": "C76",
  "text": "Technology: InfiniBand (scale-out network)\nDate: 2026-02-25\nWho said it: NVIDIA (C. Kress, CFO), Q4 FY2026 earnings call (vendor)\n\nQuote: “driven by strong adoption of NVLink, Spectrum-X Ethernet and InfiniBand.”\n\nLink: https://s201.q4cdn.com/141608511/files/doc_financials/2026/q4/NVDA-Q4-2026-Earnings-Call-25-February-2026-5_00-PM-ET.pdf"
 }
];
const INTRO = "Time needed: about 3 hours. You do not need networking knowledge.\n\nWHAT THIS IS\nA research project measures 'hype': how mature and how successful people SAY ten AI networking technologies are. We collected 76 public statements made between Nov 2025 and Nov 2026 by companies, analysts and journalists. You will rate each one independently, so we can check that our own ratings are not one person's opinion.\n\nFOR EACH STATEMENT\n1. KIND. Stage = it says what the technology has reached NOW (shipping, in production, available, a standard being written). Narrative = it says how strong or successful it is, or where it is heading (leading, the winner, not ready, losing ground). Not a claim = it only describes features or design.\n2. LEVEL 0 to 4 from the scale on the next page (skip if 'Not a claim').\n3. OTHER LEVEL only if you hesitated between two.\n4. CONFIDENCE, and an optional NOTE.\n\nRULES\n- Rate only what the statement SAYS, not whether you believe it.\n- Work alone. Do not look at the project report, slides or website, and do not search the web for opinions.\n- If a statement does two things, rate its main point.\n- A confident forecast ('will become the standard') is Narrative 3 or 4, even though it is about the future.\n- Open the link only if the quote is unclear or the statement says 'No single quote'.\n- Your answers save only when you press Submit at the end. Use 'Edit after submit' if you need a break: submit, then reopen your link.";
const SCALE = "STAGE: what has it reached now?\n0  No deployment claim (choose 'Not a claim' instead)\n1  A standard or specification is being written, or a product for a generation more than 12 months away   e.g. 'The 2.0 specification is published'\n2  Launched, available, sampling, first shipments, or deploying within 12 months   e.g. 'X is now shipping to customers'\n3  Volume or mass production, or running in production at customers   e.g. 'X is in volume production'\n4  Claimed as THE default choice   e.g. 'X is the default for every new cluster'\n\nNARRATIVE: how strong, or where heading?\n0  Declining, abandoned, only a niche, or losing share with no growth   e.g. 'X is being phased out'\n1  Not ready yet, premature, a long-term possibility, an open question   e.g. 'X simply isn't ready'\n2  A promising contender or challenger; or growing but losing share   e.g. 'X is emerging as a real alternative'\n3  Leading, winning most of the market, gaining momentum, or will dominate in about 2 years   e.g. 'X is the leading choice'\n4  Explicitly the default or standard now, or the inevitable winner   e.g. 'X will inevitably win'\n\nTIPS: 'Leading' is 3. 'Default' or 'the standard' is 4. 'Shipping' is 2; 'volume production' is 3. 'Not ready' is Narrative 1. Feature descriptions are 'Not a claim'.";
const PRACTICE = "Practice with an imaginary 'Technology Z' (answers shown):\n- 'Z switches entered volume production this quarter.' (a vendor)  ->  Stage 3\n- 'Z is the inevitable winner of the data-centre fabric war.' (an analyst)  ->  Narrative 4\n- 'Z is a promising challenger, but buyers say it is not ready.' (a journalist)  ->  Narrative 1 (main point: not ready); other level 2\n- 'Z uses a new congestion scheme with 30% lower latency.' (a vendor)  ->  Not a claim\n- 'The consortium published the Z 1.0 specification.'  ->  Stage 1";
const PER_PAGE = 4;

function buildHvdiCoderForm() {
  const form = FormApp.create('HVDI second coder questionnaire');
  form.setDescription(INTRO)
      .setCollectEmail(false)
      .setAllowResponseEdits(true)
      .setProgressBar(true)
      .setShowLinkToRespondAgain(false)
      .setConfirmationMessage('Thank you. Your ratings are saved.');
  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addPageBreakItem().setTitle('The scale (keep this page in mind; it is repeated at the top of every page)');
  form.addSectionHeaderItem().setTitle('Scale').setHelpText(SCALE);
  form.addSectionHeaderItem().setTitle('Practice').setHelpText(PRACTICE);
  CLAIMS.forEach(function (c, i) {
    if (i % PER_PAGE === 0) {
      const last = Math.min(i + PER_PAGE, CLAIMS.length);
      form.addPageBreakItem().setTitle('Statements ' + (i + 1) + ' to ' + last + ' of ' + CLAIMS.length)
          .setHelpText('Scale reminder: Stage 1 spec, 2 shipping, 3 volume production, 4 default. Narrative 1 not ready, 2 contender, 3 leading, 4 default or inevitable winner.');
    }
    form.addSectionHeaderItem().setTitle(c.code).setHelpText(c.text);
    form.addMultipleChoiceItem().setTitle(c.code + ' Kind')
        .setChoiceValues(['Stage', 'Narrative', 'Not a claim']).setRequired(true);
    form.addMultipleChoiceItem().setTitle(c.code + ' Level')
        .setHelpText('Leave blank only if you chose Not a claim.')
        .setChoiceValues(['0', '1', '2', '3', '4']);
    form.addMultipleChoiceItem().setTitle(c.code + ' Other level (only if torn)')
        .setChoiceValues(['0', '1', '2', '3', '4']);
    form.addMultipleChoiceItem().setTitle(c.code + ' Confidence')
        .setChoiceValues(['High', 'Medium', 'Low']).setRequired(true);
    form.addTextItem().setTitle(c.code + ' Note (optional)');
  });
  form.addPageBreakItem().setTitle('Finish');
  form.addTextItem().setTitle('Hours taken');
  form.addParagraphTextItem().setTitle('Any statements you found hard (codes)');
  const sheet = SpreadsheetApp.create('HVDI second coder responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
  Logger.log('Edit link (keep private): ' + form.getEditUrl());
  Logger.log('Send this link to the coder: ' + form.getPublishedUrl());
  Logger.log('Responses sheet (keep private): ' + sheet.getUrl());
}
