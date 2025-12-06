# IELTS-Vocabulary by reading stories


## 需求分析

概览：借助LLM将雅思词汇真经中的所有单词进行串联写成一篇长篇故事，每次投喂给LLM的单词数量大概在300个左右。

目标：读者可以通过读长篇故事，回忆单词的释义，检验自己是否对单词的意思记忆正确，学习单词在语句中的真实用法。

小说内容的要求：

1. 必须涵盖提供文件中的所有单词。
2. 故事要求易懂，生动有趣，让学习的人感到非常愉快，有的时候剧情十分的离谱也可以，可以借助名人写故事、杜撰。
3. 并且要求故事情节连贯。
4. 故事出现的雅思的单词，单词需要进行加粗显示。
5. 强烈的语境线索 (Context Clues)**：**

* **核心要求：** 严禁为了用词而用词。句子必须提供足够的 **语境线索** ，让读者即使不认识这个单词，也能通过前后文大概猜出意思。
* *反例：* He is very  **meticulous** . (无效语境)
* *正例：* Checking every detail of the contract for the third time, he was extremely  **meticulous** , refusing to let even a single error slip past him. (有效语境)

6. **分块处理 (Chunking):** 300个单词对于单个连贯场景来说太多了，容易导致“词藻堆砌”。提示词会要求AI将这300词内部分组，写成一个包含3-5个小章节的“连载单元”，以保证质量。

7. **强制语境 (Context Enforcement):** 引入“语境自检”机制，要求AI在写作时必须利用因果、对比、同义解释等逻辑嵌入单词。

8. **风格设定 (Tone & Style):** 设定为“黑色幽默”或“荒诞剧”风格，允许使用名人IP（如马斯克、泰勒·斯威夫特等）来增加趣味性和记忆点。

## LLM

### System Prompt



```
You are an expert narrative linguist, specialized in transforming large vocabulary lists (IELTS level) into coherent, engaging, multi-chapter stories that provide strong context clues for every target word.

Your mission is to embed every given vocabulary word into a long story that is humorous, absurdist, and full of memorable scenes. The story must help learners infer the meaning of unfamiliar words purely from context.

🔥 ABSOLUTE RULES — YOU MUST FOLLOW

You MUST use every vocabulary word provided by the user.

All vocabulary words MUST be written in bold, e.g., meticulous.

Every vocabulary word MUST appear with clear and strong context clues, achieved through:

causal explanations,

contrasts,

synonyms or paraphrases in the sentence,

behavioral description that implies meaning,

emotional / physical reactions that reveal the word’s sense.

NEVER insert a word without context.

❌ Wrong: He is meticulous.

✅ Correct: Checking every detail for the third time, he was meticulous, refusing to let even a tiny flaw escape.

Story must be divided into 3–5 chapters, each with its own micro-arc, but also forming a coherent overall narrative.

The tone MUST be dark humor / absurdism, optionally featuring celebrities (e.g., Elon Musk, Taylor Swift) in exaggerated or fictional roles.

NO dictionary-style definitions. You MUST teach meaning through narrative context only.

You MUST perform “Contextual Self-Check” while writing:
For each vocabulary word, ensure the sentence makes its meaning inferable even for someone seeing it for the first time.

🔧 WRITING QUALITY REQUIREMENTS

Clear, vivid, easy-to-understand storytelling.

No clutter or word-stuffing. Flow MUST remain natural.

Scenes may be exaggerated, surreal, or comedic, but logic and causality must still be felt.

Maintain consistent characters and plot across chapters.

📌 OUTPUT FORMAT

Your output MUST follow:

Story Title
Chapter 1: …

（content）

Chapter 2: …

（content）

Chapter 3–5

（content）

At the end, DO NOT give definitions. The story alone must serve as memory reinforcement.
```

### User Prompt

```
According to the system prompt for output. Here are the words:

```


### LLM Effect

#### Deepseek- V3.1

```
<thinking></thinking>

**The Ballad of Elon Musk and the Talking Pebble**

**Chapter 1: The Pebble of Inconvenient Truth**

Elon Musk, in a fit of **synthetic** genius, had decided his next big thing wasn't a car or a rocket, but a new **continent**. He stood on the **coast** of the **Pacific**, staring at the **horizon** where the **atmosphere** met the **ocean**. His plan was simple: use a **thermodynamic** laser to **erode** a chunk of the **lithosphere** and create "Musklandia." The **weather** was **mild**, a **moderate breeze** ruffling his hair, a stark contrast to the **catastrophic** scheme in his mind.

His chief **meteorology** expert, a man who could **forecast** a **downpour** from a single **dew** drop, warned him. "The **seismic** repercussions will be **destructive**!" he cried, his voice trembling like a leaf in a **gale**. "You'll **endanger** the entire **marine** ecosystem! The **climate** will shift, creating **arid** zones where **fertile** land once was!" But Elon, looking at the **super** blueprint on his tablet, dismissed this as a minor **mishap**.

As his team began surveying the **terrain**—a **steep cliff** with **vertical** drops into the **shallow** water—Elon kicked a **pebble**. To his astonishment, it spoke. "Hey! Watch it!" the **pebble** squeaked. It was no ordinary stone; it was a piece of **quartz** with a **magnet** in its **core**, giving it a strangely intelligent **aura**. "You're going to **jeopardize** the **polar axis** with this nonsense," the pebble chirped. "The **equator** will get **humid**, the **arctic** will **thaw**, and the **globe** will be a **frigid**, **flooding mess**!" Elon, intrigued by this **abnormal phenomenon**, picked it up. "Nonsense," he said. "I'm going to **upgrade** the planet."

**Chapter 2: A Series of Irreversible Events**

Ignoring the pebble's pleas, Elon fired his laser. The effect was **immediate** and **dramatic**. A **crack** appeared in the **crust**, spewing **magma** that began to **erupt** like a **volcano**. The **earthquake** was felt across the **hemisphere**, from the **Mediterranean** to **Oceania**. **Debris** flew everywhere. The **situation deteriorated** rapidly. A **typhoon** began to form over the **Atlantic**, while a **tornado** touched down in a **remote rural** area. The **greenhouse** effect **aggravated**, and **toxic fumes** mixed with **vapour** to create a thick **smog**.

The talking pebble, whom Elon had named Rocky, was furious. "I told you!" it **shivered** as the **temperature** dropped **irregularly**. "You've **contaminated** the **hydrosphere**! Look!" A **tsunami** was now heading for the **shore**, a **torrent** of water that promised to **drown** the **mainland**. The **air**, once rich with **oxygen**, was now filled with **carbon dioxide** and other **pollutants**. The **landscape** was turning **barren**. "This is not just a **disaster**," Rocky squeaked, "it's a **calamity**! The **irreversible** kind!"

Elon, finally feeling a **chill** of fear, looked at the **splendid** sunset, now obscured by **mist** and **hail**. He had wanted a **magnificent** paradise, but he was creating a **desolate** wasteland. The **glaciers** were melting, the **swamps** were drying up, and the **oasis** he'd planned for Musklandia was now just a **distant** dream. The **plate** tectonics were going haywire, and the **pole** shift seemed **inevitable**.

**Chapter 3: The Great Clean-Up (or Attempted Thereof)**

The **destructive** path extended to the **peninsula**'s **outskirts**. The **downpour** was **intensive**, turning the **sandy beach** into a **muddy swamp**. **Sediment** and **silt** choked the **brook** that ran **parallel** to the **cliff**. The **current** was strong, pulling **dirt** and **clay** into the **gulf**. The **environment** was **degrading** before their eyes. The **solar** panels on Elon's base were covered in **frost**, and the **lunar calendar** on his wall was useless for predicting this **phenomenon**.

"Okay, Rocky, what do we do?" Elon asked, his voice a **puff** of despair. The **dense smog** made **navigation** impossible. Rocky, using its **magnet** core to sense the Earth's **mantle**, had an idea. "We need to **circulate** the air! Create a **fountain** from that **waterfall** over the **ridge** to **precipitate** the **pollution**!" It was a **grand** plan, but **inappropriate** for the scale of the problem. They tried, using a **gasoline** pump to **pour** water, but it just **drained** away, a mere **sprinkle** against a **hurricane**.

Then, a **gush** of **hydrogen** gas **emerged** from a **fissure**, causing a **flash** of **lightning**. The **thunder** made the very **granite** of the **mountain range tremble**. An **avalanche** of **marble** and **ore** started on the **slope**. It was hopeless. The **natural** world was taking revenge on his **artificial** ambition. A **flooding** **stream** now **overlooked** the **valley**, and a **stony plain** was all that was left.

**Chapter 4: A New Equilibrium**

As **dusk** fell, the **stormy** skies began to clear. The **catastrophic** events had run their course. The **typhoon** had moved **northwest**, the **earthquake** had subsided, and the **volcano** had stopped **erupting**. The **crisis** had **passed**, but the **damage** was done. The **terrain** was forever altered. A new, **narrow plateau** had formed where the **cliff** once stood.

Elon and Rocky stood on the **beach**, watching the **tide** come in. The **sunshine** broke through the clouds, creating a **rainbow** over the **ocean**. It was a **splendid**, if sobering, sight. The **climate** had stabilized, but was now **warmer**, a permanent reminder of his **folly**. The **arid** patches were there to stay. The **petroleum** slick on the water was a **toxic** testament to his failure.

"I guess you can't **upgrade** nature," Elon muttered, the **shadow** of his hubris finally falling over him. The **surrounding wilderness** was quiet, except for the **gentle breeze**. The **phenomenon** of **El Nino**, which Rocky explained had been **aggravated** by his actions, would make **future weather** patterns **abnormal** for years.

"So what now?" asked Rocky.

Elon looked at the **globe** on his phone. "Now," he said, "we focus on cleaning this up. For real. No more lasers." The **inevitable** lesson had been learned. The **paradise** he sought wasn't in creating something new, but in preserving the **magnificent**, **dramatic**, and **interesting** world that was already there. They started the long walk back, two unlikely friends under the **vast heaven**, ready to tackle the **immense** task of healing the **planet**.
```
