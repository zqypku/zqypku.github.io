// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-services",
          title: "services",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/services/";
          },
        },{id: "news-i-joined-cispa-to-start-my-ph-d-preparatory-phase",
          title: 'I joined CISPA to start my Ph.D. (preparatory phase)!',
          description: "",
          section: "News",},{id: "news-i-have-successfully-passed-the-qualifying-exam",
          title: 'I have successfully passed the Qualifying Exam!',
          description: "",
          section: "News",},{id: "news-our-paper-named-data-poisoning-attacks-against-multimodal-encoders-was-accepted-by-icml-2023",
          title: 'Our paper named Data Poisoning Attacks Against Multimodal Encoders was accepted by ICML...',
          description: "",
          section: "News",},{id: "news-our-paper-named-securitynet-assessing-machine-learning-vulnerabilities-on-public-models-was-accepted-by-usenix-security-2024",
          title: 'Our paper named SecurityNet: Assessing Machine Learning Vulnerabilities on Public Models was accepted...',
          description: "",
          section: "News",},{id: "news-our-paper-titled-synthetic-artifact-auditing-tracing-llm-generated-synthetic-data-usage-in-downstream-applications-was-accepted-by-usenix-security-2025",
          title: 'Our paper titled Synthetic Artifact Auditing: Tracing LLM-Generated Synthetic Data Usage in Downstream...',
          description: "",
          section: "News",},{id: "news-our-paper-titled-jailbreakradar-comprehensive-assessment-of-jailbreak-attacks-against-llms-was-accepted-by-acl-2025",
          title: 'Our paper titled JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs was accepted...',
          description: "",
          section: "News",},{id: "news-our-paper-titled-hate-in-plain-sight-on-the-risks-of-moderating-ai-generated-hateful-illusions-was-accepted-by-iccv-2025",
          title: 'Our paper titled Hate in Plain Sight: On the Risks of Moderating AI-Generated...',
          description: "",
          section: "News",},{id: "news-i-am-delighted-to-be-selected-as-a-neurips-2025-reviewer-top-reviewer",
          title: 'I am delighted to be selected as a NeurIPS 2025 “Reviewer : Top...',
          description: "",
          section: "News",},{id: "news-our-paper-titled-peering-behind-the-shield-guardrail-identification-in-large-language-models-was-accepted-by-aaai-2026-aics-workshop-and-aaai-2026-trustagent-workshop",
          title: 'Our paper titled Peering Behind the Shield: Guardrail Identification in Large Language Models...',
          description: "",
          section: "News",},{id: "news-our-papers-peering-behind-the-shield-guardrail-identification-in-large-language-models-and-peercheck-enhancing-llm-generated-academic-reviews-towards-human-level-quality-were-accepted-by-acl-findings-2026",
          title: 'Our papers Peering Behind the Shield: Guardrail Identification in Large Language Models and...',
          description: "",
          section: "News",},{id: "news-our-paper-the-challenge-of-identifying-the-origin-of-black-box-large-language-models-was-accepted-by-acl-2026-privatenlp-workshop",
          title: 'Our paper The Challenge of Identifying the Origin of Black-Box Large Language Models...',
          description: "",
          section: "News",},{id: "news-our-paper-badbone-backdoor-attacks-against-backbone-models-in-visual-prompt-learning-was-accepted-by-ieee-transactions-on-information-forensics-amp-amp-security",
          title: 'Our paper BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning was...',
          description: "",
          section: "News",},{id: "news-our-paper-jades-a-universal-framework-for-jailbreak-assessment-via-decompositional-scoring-was-accepted-by-emnlp-2026-and-paper-the-challenge-of-identifying-the-origin-of-black-box-large-language-models-was-accepted-by-emnlp-findings-2026",
          title: 'Our paper JADES: A Universal Framework for Jailbreak Assessment via Decompositional Scoring was...',
          description: "",
          section: "News",},{id: "news-our-paper-jades-a-universal-framework-for-jailbreak-assessment-via-decompositional-scoring-received-a-best-paper-nomination-at-emnlp-2026",
          title: 'Our paper JADES: A Universal Framework for Jailbreak Assessment via Decompositional Scoring received...',
          description: "",
          section: "News",},{id: "news-our-paper-personahate-a-scalable-persona-based-data-synthesis-pipeline-for-hate-speech-analysis-was-accepted-by-acm-ccs-2026",
          title: 'Our paper PersonaHate: A Scalable Persona-Based Data Synthesis Pipeline for Hate Speech Analysis...',
          description: "",
          section: "News",},{id: "news-i-received-saarland-university-s-busy-beaver-best-teaching-award-for-the-ai-safety-seminar-as-head-ta",
          title: 'I received Saarland University’s “Busy Beaver” Best Teaching Award for the AI Safety...',
          description: "",
          section: "News",},{id: "news-i-was-selected-as-a-rising-star-in-eecs-2026-2027-hosted-by-the-university-of-washington-see-you-in-seattle-on-january-12-13-2027",
          title: 'I was selected as a Rising Star in EECS 2026–2027, hosted by the...',
          description: "",
          section: "News",},{id: "projects-peering-behind-the-shield-guardrail-identification-in-large-language-models",
          title: 'Peering Behind the Shield: Guardrail Identification in Large Language Models',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_guard/";
            },},{
        id: 'social-dblp',
        title: 'DBLP',
        section: 'Socials',
        handler: () => {
          window.open("https://dblp.org/pid/243/3448-2.html", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%7A%69%71%69%6E%67.%79%61%6E%67@%63%69%73%70%61.%64%65", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=AvfM2hsAAAAJ", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/focus_ziya", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
