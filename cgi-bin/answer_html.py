def print_answer(x, f_x):
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
	        <html>
	        <head>
	        	<meta charset="utf-8">
	        	<link rel="stylesheet" type="text/css" href="/style.css" />
				<title>Оптимальный план для УГА</title>
				<meta name="viewport" content="initial-scale=1.0; maximum-scale=1.0; width=device-width;">
	        </head>
	        <body>""")

	print("<div class=\"table-title\"><h3 align=\"center\">Оптимальный план</h3></div>")

	print("""
		<div>
			<div class="column">
				<table class="table-fill">
					<thead>
						<tr>
						<th class="text-center">X<sub>ik</sub></th>
	""")
	for i in range(4):
	 	print('<th class="text-center">{}</th>'.format(i+1))
	print("""
						</tr>
					</thead>
	""")
	for j in range(3):
		print('<tr><td class="text-center">{}</td>'.format(j+1))
		for i in range(4):
			print('<td>{}</td>'.format(x[j][i]))
		print('</tr>')
	print("""
				</table>
			</div>
			<br /><br /><br /><br />
			<div class=\"table-title\"><h3 align=\"center\">{}</h3></div>
			
			
		</body>
	</html>
	""".format(f_x))