OB = "{"
CB = "}"

def generateInstrument(name, shortName, clef, music):
    return f"""
    \\new Staff \\with {OB}
        instrumentName = #"{name}"
        shortInstrumentName = #"{shortName}"
    {CB}
    {OB}
        \\clef {clef}
        {music}
    {CB}
    """

def generateScore(time, staffs):
    return f"""
\\score {OB}
    <<

        \\time {time}
        {staffs}
    >>
{CB}
    """
def makeBase():
	"""
	celloOne = \\relative c {OB}
	
		{CB}
	
	celloTwo = \\relative c {OB}
	
		{CB}
	
	global = {OB}
		tempo = 3/4
		key = b \\major
	{CB}
	
	
	\\book {OB}
		\\paper {OB}
			print-all-headers = ##t
			print-page-number = ##f
		{CB}
		\\score {OB}
			<<
				\\new Staff \\with {OB}
					instrument = #"Violoncello 1"
				{CB}
				{OB}
					\\global
					\\celloOne
				{CB}
				\\new Staff \\with {OB}
		                        instrumentName = #"Violoncello 2"
		                {CB}
				{OB}
					\\global
					\\celloTwo
				{CB}
			>>
		\\header {OB}
			title = "Sous le dôme épais"
			subtitle = "for two cellos"
			composer = "Léo Delibes"
			arranger = "Krystian Figiel"
			{CB}
		{CB}
		\\pageBreak
		
		\\score {OB}
			<<
				\\new Staff \\with
				{OB}
					instrumentName = #"Violoncello 1"
				{CB}
				{OB}
					\\global
					\\celloOne
				{CB}
			>>
			\\header {OB}
			title = "Sous le dôme épais"
			subtitle = "for two cellos"
			composer = "Léo Delibes"
			arranger = "Krystian Figiel"
			{CB}	
			
		{CB}
		\\pageBreak
		\\score {OB}
			<<
				\\new Staff \\with
				{OB}
					instrumentName = #"Violoncello 2"
				{CB}
				{OB}
					\\global
					\\celloTwo
				{CB}
			>>
			\\header {OB}
			title = "Sous le dôme épais"
			subtitle = "for two cellos"
			composer = "Léo Delibes"
			arranger = "Krystian Figiel"
			{CB}
	
		{CB}
	{CB}
	
	\\version "2.18.2"
"""
