\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{assignment}[University of Minnesota College of Science and Engineering]

\LoadClass[11pt, letterpaper]{article}

\setlength{\textwidth}{6.5in}
\setlength{\textheight}{9.in}
\setlength{\oddsidemargin}{0in}
\setlength{\headheight}{0in}

\RequirePackage[margin=2cm]{geometry}
% \RequirePackage[margin=1in]{geometry} 
\RequirePackage[utf8]{inputenc}
\RequirePackage{fancybox,fancyhdr,graphicx,epsfig}
\RequirePackage{multicol,pst-plot,pstricks}
\RequirePackage{amsmath,amsfonts,amsthm,amssymb,scrextend}
\RequirePackage{enumerate,enumitem,eucal}
\RequirePackage{soul,setspace}
\RequirePackage{color}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\RequirePackage{listings}
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
\lstset{style=mystyle}

\DeclareMathOperator{\tr}{Tr}
\newcommand*{\op}[1]{\check{\mathbf#1}}
\newcommand{\bra}[1]{\langle #1 |}
\newcommand{\ket}[1]{| #1 \rangle}
\newcommand{\braket}[2]{\langle #1 | #2 \rangle}
\newcommand{\mean}[1]{\langle #1 \rangle}
\newcommand{\opvec}[1]{\check{\vec #1}}
\renewcommand{\sp}[1]{$${\begin{split}#1\end{split}}$$}

\renewcommand\maketitle{
    \begin{flushleft}
        Student Name: \name \\
        Student ID: \id \\
        Date: \todaysDate \\
    \end{flushleft}

    \begin{flushright}\vspace{-15mm}
        \includegraphics[height=2cm]{umn-logo.png}
    \end{flushright}

    \begin{center}\vspace{-1cm}
        \textbf{\large \course}\\
        \assignment \\
        \assignmentQuote
    \end{center}

    \par\noindent\rule{\textwidth}{0.4pt}

    \bigskip
    \bigskip
}

% Custom environments and commands %

% Beter center environment
\newenvironment{tightcenter}{%
    \setlength\topsep{0pt}
    \setlength\parskip{0pt}
    \begin{center}
    }{%
    \end{center}
}

% Calculus command
\newcommand{\calc}[1]{\fpeval{#1}}

% Summation command (i.e. \[ \sum_{n=1}^{\infty} 2^{-n} \])
\newcommand*{\summation}[3]{
    \sum\limits_{#1}^{#2} #3
}

% Permutation command
\newcommand*{\perm}[2]{
    \binom{#1}{#2} = {}^{#1}\!P_{#2} = \frac{#1!}{(#1 - #2)!} = \frac{#1!}{(\calc{#1 - #2})!}
}
% Combination command
\newcommand*{\comb}[2]{
    \binom{#1}{#2} = {}^{#1}C_{#2} = \frac{#1!}{#2!(#1 - #2)!} = \frac{#1!}{\calc{#2}!\calc{#1 - #2}!}
}

% Partition command (number of ways to partition a set of n objects into r cells with n1 elements
% in the first cell, n2 elements in the second cell, and so on)
\newcommand*{\partit}[3]{
    \binom{#1}{#2,#3} = \frac{#1!}{#2!#3!}
}

\newcommand*{\partits}[4]{
    \binom{#1}{#2,#3,\ldots,#4} = \frac{#1!}{#2!#3!\ldots#4!}
}

% proofs
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\I}{\mathbb{I}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\qed}{\hfill$\blacksquare$}
\let\newproof\proof
\renewenvironment{proof}{\begin{addmargin}[1em]{0em}\begin{newproof}}{\end{newproof}\end{addmargin}\qed}
% \newcommand{\expl}[1]{\text{\hfill[#1]}$}
 
\newenvironment{theorem}[2][Theorem]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{lemma}[2][Lemma]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{problem}[2][Problem]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{exercise}[2][Exercise]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{reflection}[2][Reflection]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{proposition}[2][Proposition]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{corollary}[2][Corollary]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}

% End of file %
