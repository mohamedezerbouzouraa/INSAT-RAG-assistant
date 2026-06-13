from langchain_core.documents import Document

raw_chunks = [
    "INSAT (Institut National des Sciences Appliquees et de Technologie) is a prestigious "
    
    "Tunisian public engineering school located in Centre Urbain Nord, BP 676, 1080 Tunis Cedex. "
    "It is affiliated with the University of Carthage and was established in 1992.",
    
    "INSAT was founded as part of a cultural, scientific, technical, and financial cooperation "
    "agreement between Tunisia and France. Its mission is to provide high-level scientific and "
    "technological training to support Tunisia's economic and social development.",

    "INSAT currently enrolls approximately 3,505 students. The director is Slah Ouerhani. "
    "The institution operates under the Tunisian Ministry of Higher Education and Scientific Research. "
    "The main language of instruction is French.",

    "INSAT's phone numbers are +216 71 70 38 29 and +216 71 70 39 29. "
    "The official website is https://insat.rnu.tn. "
    "The campus is located near the city center of Tunis in the Nord Urbain district.",

    "INSAT offers several degree programs: "
    "1) Diplome d'Ingenieur (5-year engineering degree) in multiple specialties. "
    "2) Licences Appliquees (3-year applied bachelor degrees). "
    "3) Masteres Professionnelles (professional master's degrees). "
    "4) Doctorat LMD (PhD program). "
    "5) Enseignement a Distance (distance learning).",

    "Engineering specialties at INSAT include: "
    "Computer Science (Informatique), Telecommunications and Networking, "
    "Software Engineering (Genie Logiciel), Industrial Computing and Automation, "
    "Industrial Biology, Industrial Chemistry, and Instrumentation and Computer Maintenance.",

    "INSAT also offers Masteres Professionnelles in various advanced technology fields, "
    "and distance-learning programs for working professionals. "
    "The doctoral school supports PhD research across all engineering disciplines.",

    "Admission to INSAT is highly competitive. Students must have obtained the Baccalaureat with "
    "the mention Tres Bien (highest honors) on the national exam to be eligible. "
    "Admission is based on national rankings from the Baccalaureat results.",

    "INSAT accepts students from different Baccalaureat tracks: "
    "CBA track (Chimie et Biologie Appliquees) for Math or Sciences Experimentales bac. "
    "MPI track (Mathematiques, Physique et Informatique) for Technical, Math, Sciences bac. "
    "After the first preparatory year (tronc commun), students choose their engineering specialization.",

    "For partner university admissions (e.g. Ohio University exchange), INSAT students must maintain "
    "an average of at least 11/20. The GRE exam is not required for graduate students.",

    "INSAT has an active research ecosystem with multiple laboratories and research units. "
    "Faculty and students work on cutting-edge projects in AI, cybersecurity, telecommunications, "
    "biotechnology, and industrial systems.",

    "The doctoral school at INSAT coordinates PhD programs and research activities. "
    "INSAT holds patents (brevets d'invention) from its applied research output. "
    "The institution hosts scientific events, conferences, and workshops throughout the year.",

    "INSAT has strong international partnerships with universities worldwide. "
    "A notable partnership exists with INSA Centre Val de Loire (France), signed June 3, 2021, "
    "covering joint research programs, teaching, and staff/student exchanges.",

    "International cooperation at INSAT includes joint research programs, exchanges of faculty, "
    "researchers, postdoctoral fellows, and technical/administrative staff. "
    "INSAT collaborates with numerous countries through bilateral agreements.",

    "The INSAT campus is modern and well-equipped, located near the center of Tunis. "
    "Facilities include advanced laboratories, research centers, a library (Bibliotheque BIRUNI), "
    "and access to the CNUDST documentation center.",

    "Student life at INSAT is vibrant and stimulating. The campus environment promotes collaboration "
    "and innovation. INSAT provides career services including internship placements, job fairs, "
    "workshops, and networking events.",

    "INSAT offers language certification programs: TOEIC (English) and DELF B2 (French). "
    "The Centre 4C supports student skills development. A Quality Cell (Cellule Qualite) "
    "oversees academic standards and continuous improvement.",

    "Administrative documents available at INSAT include: annual activity reports, enrollment forms, "
    "exam charters (charte des examens), timetables (emplois du temps), "
    "and student guides (guide de l'etudiant).",

    "INSAT graduates are highly sought after by employers in Tunisia and internationally. "
    "They are known for strong technical expertise, problem-solving skills, and adaptability.",
    "INSAT is considered one of the most selective and prestigious engineering schools in Tunisia. "
    "It ranks among the top institutions for computer science, telecommunications, "
    "and applied technology programs.",]
documents = [Document(page_content=chunk) for chunk in raw_chunks]
