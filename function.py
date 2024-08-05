def final_code_generator(latex_output):
    code1 = r"""\documentclass[12pt,a4paper]{article}
% Language and font encoding
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}

% AMS packages for math
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}

% Geometry for margins
\usepackage{geometry}
\geometry{a4paper, margin=1in}

% Package for including graphics
\usepackage{graphicx}

% Package for tables
\usepackage{array}

% Package for colors
\usepackage{xcolor}

% Package for hyperlinks
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
    pdftitle={Math Document},
    bookmarks=true,
    pdfpagemode=FullScreen,
}

% Package for including code
\usepackage{listings}
\lstset{
    basicstyle=\ttfamily,
    columns=fullflexible,
    breaklines=true
}

% Theorem environments
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}

% Custom commands
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}

\begin{document}
"""
    return f"{code1}\n{latex_output}\n\\end{{document}}"