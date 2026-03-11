The general problem of simulating (or creating) intelligence has been broken into subproblems. These consist of particular traits or capabilities that researchers expect an intelligent system to display. The traits described below have received the most attention and cover the scope of AI research.[a]

Reasoning and problem-solving
Early researchers developed algorithms that imitated step-by-step reasoning that humans use when they solve puzzles or make logical deductions.[13] By the late 1980s and 1990s, methods were developed for dealing with uncertain or incomplete information, employing concepts from probability and economics.[14]

Many of these algorithms are insufficient for solving large reasoning problems because they experience a "combinatorial explosion": They become exponentially slower as the problems grow.[15] Even humans rarely use the step-by-step deduction that early AI research could model. They solve most of their problems using fast, intuitive judgments.[16] Accurate and efficient reasoning is an unsolved problem.

Knowledge representation

An ontology represents knowledge as a set of concepts within a domain and the relationships between those concepts.
Knowledge representation and knowledge engineering[17] allow AI programs to answer questions intelligently and make deductions about real-world facts. Formal knowledge representations are used in content-based indexing and retrieval,[18] scene interpretation,[19] clinical decision support,[20] knowledge discovery (mining "interesting" and actionable inferences from large databases),[21] and other areas.[22]

A knowledge base is a body of knowledge represented in a form that can be used by a program. An ontology is the set of objects, relations, concepts, and properties used by a particular domain of knowledge.[23] Knowledge bases need to represent things such as objects, properties, categories, and relations between objects;[24] situations, events, states, and time;[25] causes and effects;[26] knowledge about knowledge (what we know about what other people know);[27] default reasoning (things that humans assume are true until they are told differently and will remain true even when other facts are changing);[28] and many other aspects and domains of knowledge.

Among the most difficult problems in knowledge representation are the breadth of commonsense knowledge (the set of atomic facts that the average person knows is enormous);[29] and the sub-symbolic form of most commonsense knowledge (much of what people know is not represented as "facts" or "statements" that they could express verbally).[16] There is also the difficulty of knowledge acquisition, the problem of obtaining knowledge for AI applications.[c]

Planning and decision-making
An "agent" is any entity (artificial or not) that perceives and takes actions in the world. A rational agent has goals or preferences and takes actions to make them happen.[d][32] In automated planning, the agent has a specific goal.[33] In automated decision-making, the agent has preferences—there are some situations it would prefer to be in, and some situations it is trying to avoid. The decision-making agent assigns a number to each situation (called the "utility") that measures how much the agent prefers it. For each possible action, it can calculate the "expected utility": the utility of all possible outcomes of the action, weighted by the probability that the outcome will occur. It can then choose the action with the maximum expected utility.[34]

In classical planning, the agent knows exactly what the effect of any action will be.[35] In most real-world problems, however, the agent may not be certain about the situation they are in (it is "unknown" or "unobservable") and it may not know for certain what will happen after each possible action (it is not "deterministic"). It must choose an action by making a probabilistic guess and then reassess the situation to see if the action worked.[36]

Alongside thorough testing and improvement based on previous decisions, having an explanation for why the agent took certain decisions is a way to build trust, especially when the decisions have to be relied upon.[37]

In some problems, the agent's preferences may be uncertain, especially if there are other agents or humans involved. These can be learned (e.g., with inverse reinforcement learning), or the agent can seek information to improve its preferences.[38] Information value theory can be used to weigh the value of exploratory or experimental actions.[39] The space of possible future actions and situations is typically intractably large, so the agents must take actions and evaluate situations while being uncertain of what the outcome will be.

A Markov decision process has a transition model that describes the probability that a particular action will change the state in a particular way and a reward function that supplies the utility of each state and the cost of each action. A policy associates a decision with each possible state. The policy could be calculated (e.g., by iteration), be heuristic, or it can be learned.[40]

Game theory describes the rational behavior of multiple interacting agents and is used in AI programs that make decisions that involve other agents.[41]

Learning
Machine learning is the study of programs that can improve their performance on a given task automatically.[42] It has been a part of AI from the beginning.[e]


In supervised learning, the training data is labelled with the expected answers, while in unsupervised learning, the model identifies patterns or structures in unlabelled data.
There are several kinds of machine learning. Unsupervised learning analyzes a stream of data and finds patterns and makes predictions without any other guidance.[45] Supervised learning requires labeling the training data with the expected answers, and comes in two main varieties: classification (where the program must learn to predict what category the input belongs in) and regression (where the program must deduce a numeric function based on numeric input).[46]

In reinforcement learning, the agent is rewarded for good responses and punished for bad ones. The agent learns to choose responses that are classified as "good".[47] Transfer learning is when the knowledge gained from one problem is applied to a new problem.[48] Deep learning is a type of machine learning that runs inputs through biologically inspired artificial neural networks for all of these types of learning.[49]

Computational learning theory can assess learners by computational complexity, by sample complexity (how much data is required), or by other notions of optimization.[50]

Natural language processing
Natural language processing (NLP) allows programs to read, write and communicate in human languages.[51] Specific problems include speech recognition, speech synthesis, machine translation, information extraction, information retrieval and question answering.[52]

Early work, based on Noam Chomsky's generative grammar and semantic networks, had difficulty with word-sense disambiguation[f] unless restricted to small domains called "micro-worlds" (due to the common sense knowledge problem[29]). Margaret Masterman believed that it was meaning and not grammar that was the key to understanding languages, and that thesauri and not dictionaries should be the basis of computational language structure.

Modern deep learning techniques for NLP include word embedding (representing words, typically as vectors encoding their meaning),[53] transformers (a deep learning architecture using an attention mechanism),[54] and others.[55] In 2019, generative pre-trained transformer (or "GPT") language models began to generate coherent text,[56][57] and by 2023, these models were able to get human-level scores on the bar exam, SAT test, GRE test, and many other real-world applications.[58]

Perception
Machine perception is the ability to use input from sensors (such as cameras, microphones, wireless signals, active lidar, sonar, radar, and tactile sensors) to deduce aspects of the world. Computer vision is the ability to analyze visual input.[59]

The field includes speech recognition,[60] image classification,[61] facial recognition, object recognition,[62] object tracking,[63] and robotic perception.[64]

Social intelligence

Kismet, a robot head which was made in the 1990s; it is a machine that can recognize and simulate emotions.[65]
Affective computing is a field that comprises systems that recognize, interpret, process, or simulate human feeling, emotion, and mood.[66] For example, some virtual assistants are programmed to speak conversationally or even to banter humorously; it makes them appear more sensitive to the emotional dynamics of human interaction, or to otherwise facilitate human–computer interaction.

However, this tends to give naïve users an unrealistic conception of the intelligence of existing computer agents.[67] Moderate successes related to affective computing include textual sentiment analysis and, more recently, multimodal sentiment analysis, wherein AI classifies the effects displayed by a videotaped subject.[68]

General intelligence
A machine with artificial general intelligence would be able to solve a wide variety of problems with breadth and versatility similar to human intelligence.[69]




Techniques
AI research uses a wide variety of techniques to accomplish the goals above.[b]

Search and optimization
There are two different kinds of search used in AI: state space search and local search:

State space search
State space search searches through a tree of possible states to try to find a goal state.[70] For example, planning algorithms search through trees of goals and subgoals, attempting to find a path to a target goal, a process called means-ends analysis.[71]

Simple exhaustive searches[72] are rarely sufficient for most real-world problems: the search space (the number of places to search) quickly grows to astronomical numbers. The result is a search that is too slow or never completes.[15] "Heuristics" or "rules of thumb" can help prioritize choices that are more likely to reach a goal.[73]

Adversarial search is used for game-playing programs, such as chess or Go. It searches through a tree of possible moves and countermoves, looking for a winning position.[74]

Local search

Illustration of gradient descent for 3 different starting points; two parameters (represented by the plan coordinates) are adjusted in order to minimize the loss function (the height)
Local search uses mathematical optimization to find a solution to a problem. It begins with some form of guess and refines it incrementally.[75]

Gradient descent is a type of local search that optimizes a set of numerical parameters by incrementally adjusting them to minimize a loss function. Variants of gradient descent are commonly used to train neural networks,[76] through the backpropagation algorithm.

Another type of local search is evolutionary computation, which aims to iteratively improve a set of candidate solutions by "mutating" and "recombining" them, selecting only the fittest to survive each generation.[77]

Distributed search processes can coordinate via swarm intelligence algorithms. Two popular swarm algorithms used in search are particle swarm optimization (inspired by bird flocking) and ant colony optimization (inspired by ant trails).[78]

Logic
Formal logic is used for reasoning and knowledge representation.[79] Formal logic comes in two main forms: propositional logic (which operates on statements that are true or false and uses logical connectives such as "and", "or", "not" and "implies")[80] and predicate logic (which also operates on objects, predicates and relations and uses quantifiers such as "Every X is a Y" and "There are some Xs that are Ys").[81]

Deductive reasoning in logic is the process of proving a new statement (conclusion) from other statements that are given and assumed to be true (the premises).[82] Proofs can be structured as proof trees, in which nodes are labelled by sentences, and children nodes are connected to parent nodes by inference rules.

Given a problem and a set of premises, problem-solving reduces to searching for a proof tree whose root node is labelled by a solution of the problem and whose leaf nodes are labelled by premises or axioms. In the case of Horn clauses, problem-solving search can be performed by reasoning forwards from the premises or backwards from the problem.[83] In the more general case of the clausal form of first-order logic, resolution is a single, axiom-free rule of inference, in which a problem is solved by proving a contradiction from premises that include the negation of the problem to be solved.[84]

Inference in both Horn clause logic and first-order logic is undecidable, and therefore intractable. However, backward reasoning with Horn clauses, which underpins computation in the logic programming language Prolog, is Turing complete. Moreover, its efficiency is competitive with computation in other symbolic programming languages.[85]

Fuzzy logic assigns a "degree of truth" between 0 and 1. It can therefore handle propositions that are vague and partially true.[86]

Non-monotonic logics, including logic programming with negation as failure, are designed to handle default reasoning.[28] Other specialized versions of logic have been developed to describe many complex domains.

Probabilistic methods for uncertain reasoning

A simple Bayesian network, with the associated conditional probability tables
Many problems in AI (including reasoning, planning, learning, perception, and robotics) require the agent to operate with incomplete or uncertain information. AI researchers have devised a number of tools to solve these problems using methods from probability theory and economics.[87] Precise mathematical tools have been developed that analyze how an agent can make choices and plan, using decision theory, decision analysis,[88] and information value theory.[89] These tools include models such as Markov decision processes,[90] dynamic decision networks,[91] game theory and mechanism design.[92]

Bayesian networks[93] are a tool that can be used for reasoning (using the Bayesian inference algorithm),[g][95] learning (using the expectation–maximization algorithm),[h][97] planning (using decision networks)[98] and perception (using dynamic Bayesian networks).[91]

Probabilistic algorithms can also be used for filtering, prediction, smoothing, and finding explanations for streams of data, thus helping perception systems analyze processes that occur over time (e.g., hidden Markov models or Kalman filters).[91]


Expectation–maximization clustering of Old Faithful eruption data starts from a random guess but then successfully converges on an accurate clustering of the two physically distinct modes of eruption.
Classifiers and statistical learning methods
The simplest AI applications can be divided into two types: classifiers (e.g., "if shiny then diamond"), on one hand, and controllers (e.g., "if diamond then pick up"), on the other hand. Classifiers[99] are functions that use pattern matching to determine the closest match. They can be fine-tuned based on chosen examples using supervised learning. Each pattern (also called an "observation") is labeled with a certain predefined class. All the observations combined with their class labels are known as a data set. When a new observation is received, that observation is classified based on previous experience.[46]

There are many kinds of classifiers in use.[100] The decision tree is the simplest and most widely used symbolic machine learning algorithm.[101] K-nearest neighbor algorithm was the most widely used analogical AI until the mid-1990s, and Kernel methods such as the support vector machine (SVM) displaced k-nearest neighbor in the 1990s.[102] The naive Bayes classifier is reportedly the "most widely used learner"[103] at Google, due in part to its scalability.[104] Neural networks are also used as classifiers.[105]

Artificial neural networks

A neural network is an interconnected group of nodes, akin to the vast network of neurons in the human brain.
An artificial neural network is based on a collection of nodes also known as artificial neurons, which loosely model the neurons in a biological brain. It is trained to recognise patterns; once trained, it can recognise those patterns in fresh data. There is an input, at least one hidden layer of nodes and an output. Each node applies a function and once the weight crosses its specified threshold, the data is transmitted to the next layer. A network is typically called a deep neural network if it has at least 2 hidden layers.[105]

Learning algorithms for neural networks use local search to choose the weights that will get the right output for each input during training. The most common training technique is the backpropagation algorithm.[106] Neural networks learn to model complex relationships between inputs and outputs and find patterns in data. In theory, a neural network can learn any function.[107]

In feedforward neural networks the signal passes in only one direction.[108] The term perceptron typically refers to a single-layer neural network.[109] In contrast, deep learning uses many layers.[110] Recurrent neural networks (RNNs) feed the output signal back into the input, which allows short-term memories of previous input events. Long short-term memory networks (LSTMs) are recurrent neural networks that better preserve longterm dependencies and are less sensitive to the vanishing gradient problem.[111] Convolutional neural networks (CNNs) use layers of kernels to more efficiently process local patterns. This local processing is especially important in image processing, where the early CNN layers typically identify simple local patterns such as edges and curves, with subsequent layers detecting more complex patterns like textures, and eventually whole objects.[112]

Deep learning

Deep learning is a subset of machine learning, which is itself a subset of artificial intelligence.[113]
Deep learning uses several layers of neurons between the network's inputs and outputs.[110] The multiple layers can progressively extract higher-level features from the raw input. For example, in image processing, lower layers may identify edges, while higher layers may identify the concepts relevant to a human such as digits, letters, or faces.[114]

Deep learning has profoundly improved the performance of programs in many important subfields of artificial intelligence, including computer vision, speech recognition, natural language processing, image classification,[115] and others. The reason that deep learning performs so well in so many applications is not known as of 2021.[116] The sudden success of deep learning in 2012–2015 did not occur because of some new discovery or theoretical breakthrough (deep neural networks and backpropagation had been described by many people, as far back as the 1950s)[i] but because of two factors: the incredible increase in computer power (including the hundred-fold increase in speed by switching to GPUs) and the availability of vast amounts of training data, especially the giant curated datasets used for benchmark testing, such as ImageNet.[j]

GPT
Generative pre-trained transformers (GPT) are large language models (LLMs) that generate text based on the semantic relationships between words in sentences. Text-based GPT models are pre-trained on a large corpus of text that can be from the Internet. The pretraining consists of predicting the next token (a token being usually a word, subword, or punctuation). Throughout this pretraining, GPT models accumulate knowledge about the world and can then generate human-like text by repeatedly predicting the next token. Typically, a subsequent training phase makes the model more truthful, useful, and harmless, usually with a technique called reinforcement learning from human feedback (RLHF). Current GPT models are prone to generating falsehoods called "hallucinations". These can be reduced with RLHF and quality data, but the problem has been getting worse for reasoning systems.[124] Such systems are used in chatbots, which allow people to ask a question or request a task in simple text.[125][126]

Current models and services include ChatGPT, Claude, Gemini, Copilot, and Meta AI.[127] Multimodal GPT models can process different types of data (modalities) such as images, videos, sound, and text.[128]

Hardware and software
Main articles: Programming languages for artificial intelligence and Hardware for artificial intelligence

Raspberry Pi AI Kit
In the late 2010s, graphics processing units (GPUs) that were increasingly designed with AI-specific enhancements and used with specialized TensorFlow software had replaced previously used central processing unit (CPUs) as the dominant means for large-scale (commercial and academic) machine learning models' training.[129] Specialized programming languages such as Prolog were used in early AI research,[130] but general-purpose programming languages like Python have become predominant.[131]

The transistor density in integrated circuits has been observed to roughly double every 18 months—a trend known as Moore's law, named after the Intel co-founder Gordon Moore, who first identified it. Improvements in GPUs have been even faster,[132] a trend sometimes called Huang's law,[133] named after Nvidia co-founder and CEO Jensen Huang.

Applications
Main article: Applications of artificial intelligence

AI Overviews, an example of AI use on search engines
AI and machine learning technology is used in most of the essential applications of the 2020s, including:

search engines (such as Google Search)
targeting online advertisements
recommendation systems (offered by Netflix, YouTube or Amazon) driving internet traffic
targeted advertising (AdSense, Facebook)
virtual assistants (such as Siri or Alexa)
autonomous vehicles (including drones, ADAS and self-driving cars)
automatic language translation (Microsoft Translator, Google Translate)
facial recognition (Apple's FaceID or Microsoft's DeepFace and Google's FaceNet)
image labeling (used by Facebook, Apple's Photos and TikTok).
The deployment of AI may be overseen by a chief automation officer (CAO).

Health and medicine
Main article: Artificial intelligence in healthcare
It has been suggested that AI can overcome discrepancies in funding allocated to different fields of research.[134]

AlphaFold 2 (2021) demonstrated the ability to approximate, in hours rather than months, the 3D structure of a protein.[135] In 2023, it was reported that AI-guided drug discovery helped find a class of antibiotics capable of killing two different types of drug-resistant bacteria.[136] In 2024, researchers used machine learning to accelerate the search for Parkinson's disease drug treatments. Their aim was to identify compounds that block the clumping, or aggregation, of alpha-synuclein (the protein that characterises Parkinson's disease). They were able to speed up the initial screening process ten-fold and reduce the cost by a thousand-fold.[137][138]

Gaming
Main article: Artificial intelligence in video games
Game playing programs have been used since the 1950s to demonstrate and test AI's most advanced techniques.[139] Deep Blue became the first computer chess-playing system to beat a reigning world chess champion, Garry Kasparov, on 11 May 1997.[140] In 2011, in a Jeopardy! quiz show exhibition match, IBM's question answering system, Watson, defeated the two greatest Jeopardy! champions, Brad Rutter and Ken Jennings, by a significant margin.[141] In March 2016, AlphaGo won 4 out of 5 games of Go in a match with Go champion Lee Sedol, becoming the first computer Go-playing system to beat a professional Go player without handicaps. Then, in 2017, it defeated Ke Jie, who was the best Go player in the world.[142] Other programs handle imperfect-information games, such as the poker-playing program Pluribus.[143] DeepMind developed increasingly generalistic reinforcement learning models, such as with MuZero, which could be trained to play chess, Go, or Atari games.[144] In 2019, DeepMind's AlphaStar achieved grandmaster level in StarCraft II, a particularly challenging real-time strategy game that involves incomplete knowledge of what happens on the map.[145] In 2021, an AI agent competed in a PlayStation Gran Turismo competition, winning against four of the world's best Gran Turismo drivers using deep reinforcement learning.[146] In 2024, Google DeepMind introduced SIMA, a type of AI capable of autonomously playing nine previously unseen open-world video games by observing screen output, as well as executing short, specific tasks in response to natural language instructions.[147]

Mathematics
In mathematics, probabilistic large language models are versatile, but can also produce wrong answers in the form of hallucinations. The Alibaba Group developed a version of its Qwen models called Qwen2-Math, that achieved state-of-the-art performance on several mathematical benchmarks, including 84% accuracy on the MATH dataset of competition mathematics problems.[148] In January 2025, Microsoft proposed the technique rStar-Math that leverages Monte Carlo tree search and step-by-step reasoning, enabling a relatively small language model like Qwen-7B to solve 53% of the AIME 2024 and 90% of the MATH benchmark problems.[149] Google DeepMind has developed models for solving mathematical problems: AlphaTensor, AlphaGeometry, AlphaProof and AlphaEvolve.[150][151]

When natural language is used to describe mathematical problems, converters can transform such prompts into a formal language such as Lean to define mathematical tasks. The experimental model Gemini Deep Think accepts natural language prompts directly and achieved gold medal results in the International Math Olympiad of 2025.[152]

Topological deep learning integrates various topological approaches.

Finance
According to Nicolas Firzli, director of the World Pensions & Investments Forum, it may be too early to see the emergence of highly innovative AI-informed financial products and services. He argues that "the deployment of AI tools will simply further automatise things: destroying tens of thousands of jobs in banking, financial planning, and pension advice in the process, but I'm not sure it will unleash a new wave of [e.g., sophisticated] pension innovation."[153]

Military
Main article: Military applications of artificial intelligence
Various countries are deploying AI military applications.[154] The main applications enhance command and control, communications, sensors, integration and interoperability.[155] Research is targeting intelligence collection and analysis, logistics, cyber operations, information operations, and semiautonomous and autonomous vehicles.[154] AI technologies enable coordination of sensors and effectors, threat detection and identification, marking of enemy positions, target acquisition, coordination and deconfliction of distributed Joint Fires between networked combat vehicles, both human-operated and autonomous.[155]

AI has been used in military operations in Iraq, Syria, Israel and Ukraine.[154][156][157][158]

Generative AI

Vincent van Gogh in watercolour created by generative AI software
These paragraphs are an excerpt from Generative artificial intelligence.[edit]
Generative artificial intelligence, also known as generative AI or GenAI, is a subfield of artificial intelligence that uses generative models to generate text, images, videos, audio, software code or other forms of data.[159] These models learn the underlying patterns and structures of their training data, and use them to generate new data[160] in response to input, which often takes the form of natural language prompts.[161][162]

The prevalence of generative AI tools has increased significantly since the AI boom in the 2020s. This boom was made possible by improvements in deep neural networks, particularly large language models (LLMs), which are based on the transformer architecture. Generative AI applications include chatbots such as ChatGPT, Claude, Copilot, DeepSeek, Google Gemini and Grok; text-to-image models such as Stable Diffusion, Flux, Midjourney, and DALL-E; and text-to-video models such as Veo, LTX and Sora.[163][164][165]

Companies in a variety of sectors have used generative AI, including those in software development, healthcare,[166] finance,[167] entertainment,[168] customer service,[169] sales and marketing,[170] art, writing,[171] and product design.[172]

Agents
Main article: Agentic AI
AI agents are software entities designed to perceive their environment, make decisions, and take actions autonomously to achieve specific goals. These agents can interact with users, their environment, or other agents. AI agents are used in various applications, including virtual assistants, chatbots, autonomous vehicles, game-playing systems, and industrial robotics. AI agents operate within the constraints of their programming, available computational resources, and hardware limitations. This means they are restricted to performing tasks within their defined scope and have finite memory and processing capabilities. In real-world applications, AI agents often face time constraints for decision-making and action execution. Many AI agents incorporate learning algorithms, enabling them to improve their performance over time through experience or training. Using machine learning, AI agents can adapt to new situations and optimise their behaviour for their designated tasks.[173][174][175]

Web search
Microsoft introduced Copilot Search in February 2023 under the name Bing Chat. Copilot Search provides AI-generated summaries.[176]

Google introduced an AI Mode at its Google I/O event on 20 May 2025.[17
Sexuality
Applications of AI in this domain include AI-enabled menstruation and fertility trackers that analyze user data to offer predictions,[178] AI-integrated sex toys (e.g., teledildonics),[179] AI-generated sexual education content,[180] and AI agents that simulate sexual and romantic partners (e.g., Replika).[181] AI is also used for the production of non-consensual deepfake pornography, raising significant ethical and legal concerns.[182]

AI technologies have also been used to attempt to identify online gender-based violence and online sexual grooming of minors.[183][184]

Other industry-specific tasks
In a 2017 survey, one in five companies reported having incorporated "AI" in some offerings or processes.[185]

In the field of evacuation and disaster managemen, AI has been used to investigate patterns in large-scale and small-scale evacuations using historical data from GPS, videos or social media.[186][187][188]

During the 2024 Indian elections, US$50 million was spent on authorized AI-generated content, notably by creating deepfakes of allied (including sometimes deceased) politicians to better engage with voters, and by translating speeches to various local languages.[189]


History
Main article: History of artificial intelligence
For a chronological guide, see Timeline of artificial intelligence.

In 2024, AI patents in China and the US numbered more than three-fourths of AI patents worldwide.[350] Though China had more AI patents, the US had 35% more patents per AI patent-applicant company than China.[350]
The study of mechanical or "formal" reasoning began with philosophers and mathematicians in antiquity. The study of logic led directly to Alan Turing's theory of computation, which suggested that a machine, by shuffling symbols as simple as "0" and "1", could simulate any conceivable form of mathematical reasoning.[351][352] This, along with concurrent discoveries in cybernetics, information theory and neurobiology, led researchers to consider the possibility of building an "electronic brain".[r] They developed several areas of research that would become part of AI,[354] such as McCulloch and Pitts design for "artificial neurons" in 1943,[117] and Turing's influential 1950 paper 'Computing Machinery and Intelligence', which introduced the Turing test and showed that "machine intelligence" was plausible.[355][352]

The field of AI research was founded at a workshop at Dartmouth College in 1956.[s][6] The attendees became the leaders of AI research in the 1960s.[t] They and their students produced programs that the press described as "astonishing":[u] computers were learning checkers strategies, solving word problems in algebra, proving logical theorems and speaking English.[v][7] Artificial intelligence laboratories were set up at a number of British and U.S. universities in the latter 1950s and early 1960s.[352]

Researchers in the 1960s and the 1970s were convinced that their methods would eventually succeed in creating a machine with general intelligence and considered this the goal of their field.[359] In 1965 Herbert Simon predicted, "machines will be capable, within twenty years, of doing any work a man can do".[360] In 1967 Marvin Minsky agreed, writing that "within a generation ... the problem of creating 'artificial intelligence' will substantially be solved".[361] They had, however, underestimated the difficulty of the problem.[w] In 1974, both the U.S. and British governments cut off exploratory research in response to the criticism of Sir James Lighthill[363] and ongoing pressure from the U.S. Congress to fund more productive projects.[364] Minsky and Papert's book Perceptrons was understood as proving that artificial neural networks would never be useful for solving real-world tasks, thus discrediting the approach altogether.[365] The "AI winter", a period when obtaining funding for AI projects was difficult, followed.[9]

In the early 1980s, AI research was revived by the commercial success of expert systems,[366] a form of AI program that simulated the knowledge and analytical skills of human experts. By 1985, the market for AI had reached over a billion dollars. At the same time, Japan's fifth generation computer project inspired the U.S. and British governments to restore funding for academic research.[8] However, beginning with the collapse of the Lisp Machine market in 1987, AI once again fell into disrepute, and a second, longer-lasting winter began.[10]

Up to this point, most of AI's funding had gone to projects that used high-level symbols to represent mental objects like plans, goals, beliefs, and known facts. In the 1980s, some researchers began to doubt that this approach would be able to imitate all the processes of human cognition, especially perception, robotics, learning and pattern recognition,[367] and began to look into "sub-symbolic" approaches.[368] Rodney Brooks rejected "representation" in general and focussed directly on engineering machines that move and survive.[x] Judea Pearl, Lotfi Zadeh, and others developed methods that handled incomplete and uncertain information by making reasonable guesses rather than precise logic.[87][373] But the most important development was the revival of "connectionism", including neural network research, by Geoffrey Hinton and others.[374] In 1990, Yann LeCun successfully showed that convolutional neural networks can recognize handwritten digits, the first of many successful applications of neural networks.[375]

AI gradually restored its reputation in the late 1990s and early 21st century by exploiting formal mathematical methods and by finding specific solutions to specific problems. This "narrow" and "formal" focus allowed researchers to produce verifiable results and collaborate with other fields (such as statistics, economics and mathematics).[376] By 2000, solutions developed by AI researchers were being widely used, although in the 1990s they were rarely described as "artificial intelligence" (a tendency known as the AI effect).[377] However, several academic researchers became concerned that AI was no longer pursuing its original goal of creating versatile, fully intelligent machines. Beginning around 2002, they founded the subfield of artificial general intelligence (or "AGI"), which had several well-funded institutions by the 2010s.[69]

Deep learning began to dominate industry benchmarks in 2012 and was adopted throughout the field.[11] For many specific tasks, other methods were abandoned.[y] Deep learning's success was based on both hardware improvements (faster computers,[379] graphics processing units, cloud computing[380]) and access to large amounts of data[381] (including curated datasets,[380] such as ImageNet). Deep learning's success led to an enormous increase in interest and funding in AI.[z] The amount of machine learning research (measured by total publications) increased by 50% in the years 2015–2019.[335]


The number of Google searches for the term "AI" accelerated in 2022.
In 2016, issues of fairness and the misuse of technology were catapulted into center stage at machine learning conferences, publications vastly increased, funding became available, and many researchers re-focussed their careers on these issues. The alignment problem became a serious field of academic study.[312]

In the late 2010s and early 2020s, AGI companies began to deliver programs that created enormous interest. In 2015, AlphaGo, developed by DeepMind, beat the world champion Go player. The program taught only the game's rules and developed a strategy by itself. GPT-3 is a large language model that was released in 2020 by OpenAI and is capable of generating high-quality human-like text.[382] ChatGPT, launched on 30 November 2022, became the fastest-growing consumer software application in history, gaining over 100 million users in two months.[383] It marked what is widely regarded as AI's breakout year, bringing it into the public consciousness.[384] These programs, and others, inspired an aggressive AI boom, where large companies began investing billions of dollars in AI research. According to AI Impacts, about US$50 billion annually was invested in "AI" around 2022 in the U.S. alone and about 20% of the new U.S. Computer Science PhD graduates have specialized in "AI".[385] About 800,000 "AI"-related U.S. job openings existed in 2022.[386] According to PitchBook research, 22% of newly funded startups in 2024 claimed to be AI companies.[387]