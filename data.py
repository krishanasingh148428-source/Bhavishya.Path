# Stream codes: m=PCM, x=PCMB, b=PCB, c=Commerce, h=Humanities, a=AI & CS
STREAM_NAMES = {"m": "PCM", "x": "PCMB", "b": "PCB", "c": "Commerce", "h": "Humanities", "a": "AI & CS"}

STREAMS = {
 "science": ("Science", "Physics and Chemistry with Maths and/or Biology", "🔬",
   [("PCM: Physics, Chemistry, Maths", "m", []), ("PCMB: Physics, Chemistry, Maths, Biology", "x", []), ("PCB: Physics, Chemistry, Biology", "b", [])]),
 "commerce": ("Commerce", "Accountancy, Business Studies, Economics", "📊",
   [("Commerce with Maths", "c", []), ("Commerce without Maths", "c", ["Actuary", "Data / Business Analyst"])]),
 "humanities": ("Humanities / Arts", "History, Political Science, Geography, Psychology, Sociology", "🎨",
   [("Humanities with Maths / Economics", "h", []), ("Humanities without Maths", "h", ["Economist / Policy Analyst"])]),
 "ai": ("AI & Computer Science", "Coding, AI, data and tech careers for any stream", "🤖",
   [("All AI & CS careers", "a", [])]),
}

# name|streams|qualification & pathway|entrance exams|salary LPA (low-high)|scope
RAW = """Software Engineer|mxa|B.Tech/B.E. in CSE or IT (4 yrs), or BCA + MCA. Learn Python, Java, C++.|JEE Main, JEE Advanced, BITSAT, state CETs|4-15|Top product firms pay 30+ LPA; global remote jobs and startups.
Data Scientist|mxa|B.Tech CSE/Data Science or B.Sc Statistics/Maths. Learn Python, SQL, Machine Learning.|JEE Main, CUET|6-14|High demand in banking, healthcare and e-commerce.
AI & ML Engineer|ma|B.Tech in AI & ML or CSE. Strong Maths (linear algebra, calculus) needed.|JEE Main, VITEEE, SRMJEEE|7-15|Fastest-growing, high-paying field in the generative AI era.
Cyber Security Expert|ma|B.Tech Cyber Security/CSE, or BCA + CEH/CISSP. Learn Linux, networking, penetration testing.|JEE Main, CUET, university tests|5-10|Every bank and tech company needs experts; 25+ LPA with experience.
Robotics & Automation Engineer|ma|B.Tech in Robotics, Mechatronics, Electronics or Mechanical. Build Arduino/Raspberry Pi projects.|JEE Main, state CETs|5-10|Smart factories, surgical robots, defence drones.
Web & App Developer|a|BCA/B.Tech CSE or self-learning. HTML, CSS, JavaScript, Python, Flutter. (Salary approximate)|CUET, JEE Main (for B.Tech)|3.5-10|Freelancing, startups and remote work are common.
Cloud & DevOps Engineer|a|B.Tech/BCA plus AWS, Azure or Google Cloud certifications. (Salary approximate)|JEE Main, CUET, cloud certification exams|5-12|Companies are moving to the cloud; steady demand.
Game Developer|a|B.Tech CSE, BCA or game design diploma. Learn Unity, Unreal, C#. (Salary approximate)|CUET, university tests|3.5-9|Growing Indian gaming industry and studios abroad.
Commercial Pilot|mx|12th PCM with 50%+, DGCA Class 1 & 2 medical, CPL with 200 flying hours.|DGCA-approved flying schools, IndiGo/Air India cadet programs|12-36|Captains earn 50+ LPA; demand rising with aviation growth.
Mechanical Engineer|m|4-year B.Tech/B.E. in Mechanical Engineering. CAD/CAM and robotics are a plus.|JEE Main, JEE Advanced, state CETs|3.5-8|PSUs and automobile giants pay 12-18 LPA; EV and aerospace scope.
Civil Engineer|m|4-year B.Tech/B.E. in Civil Engineering.|JEE Main, state CETs; GATE, SSC JE, IES for govt jobs|3.5-7|Govt jobs and project managers earn 12+ LPA; smart cities and highways.
Electrical & Electronics Engineer|m|B.Tech/B.E. in Electrical (EE) or Electronics & Communication (ECE).|JEE Main, JEE Advanced, GATE (for PSUs)|4-9|Power grids, semiconductors, renewable energy, telecom.
Aerospace Engineer|mx|B.Tech in Aerospace/Aeronautical Engineering.|JEE Advanced (IITs, IIST)|6-12|ISRO, DRDO, HAL, private space startups like Skyroot.
Architect|mx|5-year B.Arch. Need drawing skills, AutoCAD, Revit.|NATA, JEE Main Paper 2|4-8|Own firm has no earning limit; urban development and interiors.
Indian Armed Forces (NDA / Technical Entry)|m|12th PCM, then NDA or Technical Entry Scheme (TES).|NDA (UPSC), JEE Main + SSB interview|8.4-10.8|Free medical, housing, pension and great respect.
Merchant Navy Officer|mx|12th PCM 60%+ (English 50%). B.Sc Nautical Science or B.Tech Marine Engineering.|IMU-CET|10-18|Captain or Chief Engineer can earn 70+ LPA (tax-free NRI status).
Research Scientist (ISRO / DRDO / BARC)|m|B.Tech or B.Sc + M.Sc in Physics, Chemistry or Maths; BS-MS dual degree.|IAT (IISER), NEST (NISER), JEE, GATE, ICRB|9.6-12|Space research, defence technology, nuclear science.
Statistician / Operations Research Analyst|m|B.Stat or B.Sc in Statistics/Maths. Learn data modelling and probability.|ISI entrance, CUET|5-20|ISI graduates earn 12-20 LPA; logistics, supply chain, analytics.
Actuary|mxc|Maths/Statistics/B.Com graduation plus actuarial papers (13 in total).|ACET (IAI)|6-12|Fellow actuaries earn 30-50+ LPA; insurance, banking, pensions.
Forensic Scientist|mxb|B.Sc in Forensic Science (3 yrs) then M.Sc. Chemistry, physics, ballistics help.|CUET, AIFSET, NFSU entrance|4-7|CBI, IB, police and state forensic labs.
Doctor (MBBS)|xb|5.5-year MBBS (with internship), then MD/MS for specialisation.|NEET-UG|6-12|Specialists earn 25-60 LPA; most respected career.
Dentist (BDS)|xb|5-year BDS (4 yrs + 1 yr internship), then MDS.|NEET-UG|4-7|Own clinic increases income; good work-life balance.
Ayurvedic / Homeopathic Doctor (BAMS / BHMS)|xb|5.5-year BAMS or BHMS degree via AYUSH counselling.|NEET-UG|4-8|Govt AYUSH hospitals or own clinic; growing herbal-care demand.
Veterinary Doctor|xb|5.5-year B.V.Sc & A.H.|NEET-UG, state veterinary exams|5-9.6|Govt dairy, wildlife, zoos and pet clinics.
Pharmacist|xb|4-year B.Pharm (or 6-year Pharm.D) plus state pharmacy council registration.|State CETs (MHT-CET, WBJEE), CUET|3-6|Pharma companies, drug inspector or own medical store.
Biotechnologist|xb|B.Sc (3 yrs) or B.Tech (4 yrs) in Biotechnology; M.Sc helps.|CUET, JEE Main, university tests|4-7.5|Vaccines, genetics, agriculture; 15+ LPA in research.
Bioinformatics Specialist|xb|B.Sc or B.Tech in Bioinformatics. Biology plus computer science.|Science entrance exams, CUET|5-9|IT firms, genetic research labs, pharma.
Biomedical Engineer|x|4-year B.Tech in Biomedical Engineering (MRI machines, pacemakers).|JEE Main, VITEEE, SRMJEEE|4.5-8|Medical device companies and hospitals.
Physiotherapist|xb|4.5-year BPT (6-month internship included).|State exams, CUET, college merit|3.5-6|Sports teams, hospitals, own rehab centre.
Environmental Scientist|x|B.Sc in Environmental Science, then M.Sc.|CUET, university tests|4-7|Climate change, pollution control, green energy.
Agricultural Scientist|xb|4-year B.Sc (Hons) Agriculture.|ICAR AIEEA (via CUET), state exams|4.5-8|Govt agriculture, bank AFO, seed and agro-tech firms.
Food Technologist|x|B.Tech or B.Sc in Food Technology.|CUET, ICAR AIEEA|4-7|Food quality, new products, food safety.
Nursing Officer|b|4-year B.Sc Nursing, then state nursing council licence.|NEET, AIIMS Nursing|3.6-8.4|Huge demand abroad (UK, Canada, Australia).
Nutritionist & Dietitian|b|3-year B.Sc in Nutrition & Dietetics or Home Science; Registered Dietitian exam.|Merit, CUET|3-6|Hospitals, fitness centres, online consultations.
Microbiologist|b|3-year B.Sc Microbiology; M.Sc/PhD for research.|CUET, merit|3-6|Pathology labs, food, pharma, research institutes.
Medical Lab Technologist (BMLT)|b|3-year B.Sc in Medical Laboratory Technology.|State paramedical exams, merit|2.4-4.8|Hospitals and diagnostic chains; open own lab.
Radiology & Imaging Technologist|b|3-year B.Sc Radiology (X-Ray, MRI, CT, ultrasound).|Paramedical entrance, merit|3-6.6|Skilled radiographers are always in shortage.
Optometrist|b|4-year Bachelor of Optometry.|University entrance, merit|3-5.4|Eye hospitals, Lenskart-type brands, own optical shop.
Genetic Engineer|b|B.Sc or B.Tech in Genetics/Genetic Engineering, then M.Sc/PhD.|CUET, private tests|4.8-9.6|Gene therapy, DNA research, improved crops.
Occupational Therapist (BOT)|b|4.5-year Bachelor of Occupational Therapy.|Paramedical entrance, merit|3.6-6.6|Special schools, rehab centres, mental health hospitals, NGOs.
Clinical Psychologist / Counsellor|bh|BA/B.Sc Psychology, then MA/M.Sc and M.Phil with RCI licence.|CUET, merit|4-8|Private practice can reach 12-20 LPA; mental health demand is rising.
Chartered Accountant (CA)|mc|Register with ICAI: CA Foundation, Intermediate, Final plus articleship.|CA Foundation|7-12|Big Four firms or own practice; auditing, tax, finance.
Company Secretary (CS)|c|ICSI: CSEET, CS Executive, CS Professional plus 21-month training.|CSEET|5-9|Every listed company must appoint a CS.
Cost & Management Accountant (CMA)|c|ICMAI: Foundation, Intermediate, Final plus 15-month training.|CMA Foundation|6-10|Corporate and public sector costing roles.
Chartered Financial Analyst (CFA)|c|Bachelor's degree (B.Com/BBA/BMS) plus CFA Levels 1-3 and 4,000 work hours.|CFA exams|8-15|Mutual funds, hedge funds, global investment banks.
Certified Public Accountant (CPA)|c|Commerce/accounting degree plus extra credits; US CPA exam (4 sections).|AICPA CPA exam|7-12|US GAAP, international tax, global remote roles.
Investment Banker|c|B.Com (Hons)/BBA Finance/BMS, then MBA Finance (IIM); CA or CFA helps.|IPMAT, CUET, CAT|10-20|One of the highest-paying commerce careers.
Financial Planner & Wealth Manager|c|B.Com/BBA plus CFP certification (FPSB India).|CFP exams|4-8|Private banks, wealth firms or independent advisor.
Business Management (BBA / MBA)|c|3-year BBA or 5-year Integrated MBA, then MBA.|IPMAT, CUET, SET, CAT|4-25|Top MBA earns 12-25 LPA; management trainee roles.
Digital Marketing & Brand Manager|ch|BBA/B.Com/Mass Media plus Google and Meta certifications; SEO, ads, analytics.|CUET, college tests|4-22|Agencies, startups, freelancing; Brand Head earns up to 22 LPA.
HR Manager|ch|BBA HR, B.Com, BA Psychology; MBA/MA in HRM (XLRI, TISS).|CUET, XAT, CAT|3.5-25|Top B-school MBA gives 15-25 LPA; path to CHRO.
Supply Chain & Logistics Manager|c|BBA/B.Com in Logistics, then MBA in Operations.|CUET, CAT|5-9|E-commerce and quick-commerce boom.
Entrepreneur / Startup Founder|c|BBA/B.Com helps; no degree required. Validate ideas in college incubators.|None required|0-0|Earnings have no upper limit but involve risk.
Retail & E-Commerce Manager|c|BBA Retail Management or B.Com plus PG diploma in retail/e-commerce.|CUET, college tests|4-7.5|Amazon, large retail chains, marketplaces.
Lawyer (Corporate & Litigation)|ch|5-year integrated BA LLB / BBA LLB / B.Com LLB at NLUs.|CLAT, AILET, SLAT|6-16|Senior lawyers earn 25-50 LPA; judiciary exams possible.
Economist / Policy Analyst|mch|BA (Hons)/B.Sc Economics, then MA/M.Sc. Maths and Economics help.|CUET, ISI and college tests|6-14|RBI, NITI Aayog, banks; seniors 25+ LPA.
Data / Business Analyst|ca|BBA Business Analytics, B.Com with data certification, or BCA. Excel, SQL, Python, Power BI.|CUET, college tests|5-9|Almost every company hires analysts.
Hotel & Hospitality Manager|ch|3-year B.Sc Hospitality & Hotel Administration (IHM).|NCHMCT JEE|3.5-7|Taj, Oberoi, Marriott, cruise lines; GM abroad 18-35 LPA.
UI/UX Designer|mcha|B.Des or any degree with UI/UX specialisation. Figma, Adobe XD, user psychology.|UCEED, NID DAT, NIFT|5-11|Tech startups and apps; 18-30 LPA with experience.
Event Manager & PR Specialist|ch|BBA Event Management, Mass Communication or PR degree/diploma.|CUET, college tests|3.5-6.5|Own event company can earn 12-22 LPA.
Civil Services (IAS, IPS, IFS)|h|Graduation in any subject, then UPSC Civil Services (Prelims, Mains, Interview).|UPSC CSE|7-12|District Magistrate, SP or Diplomat with govt bungalow and perks.
Journalism & Mass Communication|h|BJMC or BA Media Studies (IIMC, Symbiosis, XIC).|IIMC, Symbiosis, XIC tests|3.5-6|Anchors and editors earn 15-30 LPA.
Fashion Designer|h|B.Des in Fashion Design (NIFT).|NIFT Entrance|4-8|Own brand or luxury label can earn 15-25 LPA.
Interior Designer|h|B.Des or B.Sc in Interior Design (CEPT, NID).|NID DAT, CEPT tests|4-7|Own consultancy can earn 15-25 LPA.
Teacher & Professor|h|BA + MA, then B.Ed and CTET/STET (school) or UGC NET (college).|CTET, STET, UGC NET|5-12|Secure govt jobs; professors reach 20+ LPA.
Social Work (MSW) & CSR|h|BSW or BA, then MSW (TISS Mumbai).|TISS entrance|6-10|NGOs, UNICEF, WHO, company CSR teams.
Content Writer & Editor|h|BA in English, Journalism or Mass Communication plus writing portfolio and SEO basics.|College tests|3.5-6|Freelance and work-from-home friendly; heads earn 10-18 LPA.
Foreign Language Specialist / Translator|h|BA (Hons) in French, German, Spanish, Japanese or Mandarin (JNU, EFLU, DU).|CUET, JNU, EFLU tests|5-9|MNCs, embassies, tourism, IT firms.
Archaeologist & Museologist|h|BA History/Archaeology, then MA or ASI PG Diploma.|University tests|5-8|ASI and govt museums; research projects up to 18 LPA.
Filmmaker, Director & Screenwriter|h|Graduation in Film Studies/Mass Communication; courses at FTII, SRFTI, Whistling Woods.|FTII, SRFTI tests|4-7|OTT boom; a successful project can reach 15-50+ LPA.
Aviation: Cabin Crew & Airport Management|h|12th pass for cabin crew, or BBA Aviation Management. Communication, grooming, fitness.|Airline recruitment, college tests|5-8|Emirates/Qatar pay 12-22 LPA with tax-free allowances.
International Relations & Diplomacy|h|BA then MA in Political Science/IR (JNU, Ashoka, Jamia).|CUET, JNU tests|5-9|UN, embassies, think-tanks; UN pay 15-30 LPA."""

CAREERS = []
for i, line in enumerate(RAW.strip().splitlines()):
    n, s, p, e, sal, sc = line.split("|")
    lo, hi = (float(x) for x in sal.split("-"))
    txt = "Variable (no upper limit)" if hi == 0 else "₹%g to ₹%g LPA" % (lo, hi)
    CAREERS.append(dict(id=i, name=n, streams=s, path=p, exams=e, lo=lo, hi=hi, sal=txt, scope=sc))
