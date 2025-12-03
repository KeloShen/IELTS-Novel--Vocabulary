// ==========================================
// The Absurd Ark - Typst Template (Fixed for Mac)
// ==========================================

// 1. Global Color Palette (Modern & Academic)
#let primary-color = rgb("#2c3e50") // Dark Blue/Grey
#let accent-color = rgb("#e74c3c")  // Red for Highlights/Vocab
#let box-bg = rgb("#f4f6f7")        // Light Grey for summary boxes

// 2. Helper Function: Vocabulary Highlighting
#let vocab(word) = {
  text(fill: accent-color, weight: "bold", word)
}

// 3. Helper Function: Chapter Summary Box
#let chapter_info(focus: "", plot: "") = {
  block(
    fill: box-bg,
    stroke: (left: 4pt + primary-color),
    inset: 1em,
    width: 100%,
    radius: 4pt,
    [
      *Focus:* #focus \
      *Plot:* #plot
    ]
  )
}

// 4. Main Project Function
#let project(
  title: "",
  subtitle: "",
  author: "",
  body
) = {
  // --- Document Metadata ---
  set document(author: author, title: title)
  
  // --- Page Setup ---
  set page(
    paper: "a4",
    margin: (x: 2.5cm, y: 2.5cm),
    numbering: "1",
    // Header
    header: context {
      if counter(page).get().first() > 1 {
        [
          #set text(style: "italic", size: 9pt, fill: gray)
          #title 
          #h(1fr) 
          Chapter #counter(heading).display()
        ]
      }
    }
  )

  // --- Font & Paragraph Setup ---
  // Fix 1: Added fallback fonts for Mac (Times New Roman, PingFang SC for Chinese compatibility)
  set text(font: ("Linux Libertine", "Times New Roman", "PingFang SC"), lang: "en", size: 11pt)
  set par(justify: true, leading: 0.8em, first-line-indent: 2em)

  // --- Heading Styles ---
  // Level 1 Heading (Chapter Title)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(2em)
    align(center)[
      // Fix 1: Fallback fonts for headings (Arial)
      #text(font: ("Linux Biolinum", "Arial", "Helvetica"), size: 14pt, weight: "bold", fill: gray)[CHAPTER #counter(heading).display()]
      #v(0.5em)
      #text(font: ("Linux Biolinum", "Arial", "Helvetica"), size: 24pt, weight: "black", fill: primary-color)[#it.body]
      #v(0.5em)
      #line(length: 60%, stroke: 1pt + gray)
    ]
    v(2em)
  }

  // Level 2 Heading (Subsections)
  show heading.where(level: 2): it => {
    v(1em)
    // Fix 1: Fallback fonts
    text(font: ("Linux Biolinum", "Arial", "Helvetica"), size: 14pt, weight: "bold", fill: primary-color, it.body)
    v(0.5em)
  }

// --- Title Page Construction ---
  {
    set page(header: none, numbering: none) 
    align(center + horizon)[
      #v(-2em)
      #rect(width: 100%, stroke: 2pt + primary-color)[
        #v(1em)
        // Fix 1: Fallback fonts
        #text(size: 3em, weight: "black", font: ("Linux Biolinum", "Arial", "Helvetica"), fill: primary-color)[#title] \
        #v(0.5em)
        #text(size: 1.5em, style: "italic", fill: gray)[#subtitle]
        #v(1em)
      ]
      
      #v(4em)
      
      // ============================================
      // 这里是修改的地方：替换掉原来的 circle 和 placeholder text
      // 确保你的图片文件名为 cover.jpg，或者修改下面的文件名
      // ============================================
      #image("cover.jpg", width: 80%)

      #v(1fr)
      #text(size: 1.2em)[Written by] \
      #text(size: 1.5em, weight: "bold")[#author]
      #v(2em)
    ]
  }

  // --- Table of Contents ---
  pagebreak()
  show outline.entry: it => {
    v(0.2em)
    it
  }
  // Fix 2: Changed indent: true to indent: auto to fix compilation error
  outline(title: text(font: ("Linux Biolinum", "Arial", "Helvetica"), fill: primary-color)[Table of Contents], indent: auto)
  
  // --- Main Content Body ---
  pagebreak()
  body
}