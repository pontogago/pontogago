async function enviarScript(scriptText){
	const lines = scriptText.split(/[\n\t]+/).map(line => line.trim()).filter(line => line);
	main = document.querySelector("#main"),
	textarea = main.querySelector(`div[contenteditable="true"]`)
	
	if(!textarea) throw new Error("Não há uma conversa aberta")
	
	for(const line of lines){
		console.log(line)
	
		textarea.focus();
		document.execCommand('insertText', false, line);
		textarea.dispatchEvent(new Event('change', {bubbles: true}));
	
		setTimeout(() => {
			(main.querySelector(`[data-testid="send"]`) || main.querySelector(`[data-icon="send"]`)).click();
		}, 100);
		
		if(lines.indexOf(line) !== lines.length - 1) await new Promise(resolve => setTimeout(resolve, 250));
	}
	
	return lines.length;
}

enviarScript(`
1 elefante incomoda muita gente,
2 elefantes incomodam muito mais,
3 elefantes incomodam muita gente,
4 elefantes incomodam demais,
5 elefantes incomodam muita gente,
6 elefantes incomodam demais,
7 elefantes incomodam muita gente,
8 elefantes incomodam demais,
9 elefantes incomodam muita gente,
10 elefantes incomodam demais,
11 elefantes incomodam muita gente,
12 elefantes incomodam demais,
13 elefantes incomodam muita gente,
14 elefantes incomodam demais,
15 elefantes incomodam muita gente,
16 elefantes incomodam demais,
17 elefantes incomodam muita gente,
18 elefantes incomodam demais,
19 elefantes incomodam muita gente,
20 elefantes incomodam demais,
21 elefantes incomodam muita gente,
22 elefantes incomodam demais,
23 elefantes incomodam muita gente,
24 elefantes incomodam demais,
25 elefantes incomodam muita gente,
26 elefantes incomodam demais,
27 elefantes incomodam muita gente,
28 elefantes incomodam demais,
29 elefantes incomodam muita gente,
30 elefantes incomodam demais,
31 elefantes incomodam muita gente,
32 elefantes incomodam demais,
33 elefantes incomodam muita gente,
34 elefantes incomodam demais,
35 elefantes incomodam muita gente,
36 elefantes incomodam demais,
37 elefantes incomodam muita gente,
38 elefantes incomodam demais,
39 elefantes incomodam muita gente,
40 elefantes incomodam demais,
41 elefantes incomodam muita gente,
42 elefantes incomodam demais,
43 elefantes incomodam muita gente,
44 elefantes incomodam demais,
45 elefantes incomodam muita gente,
46 elefantes incomodam demais,
47 elefantes incomodam muita gente,
48 elefantes incomodam muita gente,
49 elefantes incomodam muita gente,
50 elefantes incomodam demais,
51 elefantes incomodam muita gente,
52 elefantes incomodam demais,
53 elefantes incomodam muita gente,
54 elefantes incomodam demais,
55 elefantes incomodam muita gente,
56 elefantes incomodam demais,
57 elefantes incomodam muita gente,
58 elefantes incomodam demais,
59 elefantes incomodam muita gente,
60 elefantes incomodam demais,
61 elefantes incomodam muita gente,
62 elefantes incomodam demais,
63 elefantes incomodam muita gente,
64 elefantes incomodam demais,
65 elefantes incomodam muita gente,
66 elefantes incomodam demais,
67 elefantes incomodam muita gente,
68 elefantes incomodam demais,
69 elefantes incomodam muita gente,
70 elefantes incomodam demais,
71 elefantes incomodam muita gente,
72 elefantes incomodam muita gente,
73 elefantes incomodam muita gente,
74 elefantes incomodam muita gente,
75 elefantes incomodam muita gente,
76 elefantes incomodam muita gente,
77 elefantes incomodam muita gente,
78 elefantes incomodam muita gente,
79 elefantes incomodam muita gente,
80 elefantes incomodam muita gente,
81 elefantes incomodam muita gente,
82 elefantes incomodam muita gente,
83 elefantes incomodam muita gente,
84 elefantes incomodam muita gente,
85 elefantes incomodam muita gente,
86 elefantes incomodam muita gente,
87 elefantes incomodam muita gente,
88 elefantes incomodam muita gente,
89 elefantes incomodam muita gente,
90 elefantes incomodam muita gente,
91 elefantes incomodam muita gente,
92 elefantes incomodam muita gente,
93 elefantes incomodam muita gente,
94 elefantes incomodam muita gente,
95 elefantes incomodam muita gente,
96 elefantes incomodam muita gente,
97 elefantes incomodam muita gente,
98 elefantes incomodam muita gente,
99 elefantes incomodam muita gente,
100 elefantes incomodam muita gente!


`).then(e => console.log(`Código finalizado, ${e} mensagens enviadas`)).catch(console.error)
