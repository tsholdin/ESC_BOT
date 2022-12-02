def second():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1957"
    df = pd.read_html(url,match="Points")
    second = df[0]
    second.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(second)
    second.Points = pd.to_numeric(second.Points)
    second.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1957 \nFrankfurt, West Germany", color="black")
def third():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1958"
    df = pd.read_html(url,match="Points")
    third = df[0]
    third.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(third)
    third.Points = pd.to_numeric(third.Points)
    third.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1958 \nHilversum, Netherlands", color="black")
def fourth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1959"
    df = pd.read_html(url,match="Points")
    fourth = df[0]
    fourth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourth)
    fourth.Points = pd.to_numeric(fourth.Points)
    fourth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1959 \nCannes, France", color="black")
def fifth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1960"
    df = pd.read_html(url,match="Points")
    fifth = df[0]
    fifth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fifth)
    fifth.Points = pd.to_numeric(fifth.Points)
    fifth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1960 \nLondon, United Kingdom", color="black")
def sixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1961"
    df = pd.read_html(url,match="Points")
    sixth = df[0]
    sixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixth)
    sixth.Points = pd.to_numeric(sixth.Points)
    sixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1961 \nCannes, France", color="black")
def seventh():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1962"
    df = pd.read_html(url,match="Points")
    seventh = df[0]
    seventh.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(seventh)
    seventh.Points = pd.to_numeric(seventh.Points)
    seventh.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1962 \nLuxembourg City, Luxembourg", color="black")
def eighth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1963"
    df = pd.read_html(url,match="Points")
    eighth = df[0]
    eighth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(eighth)
    eighth.Points = pd.to_numeric(eighth.Points)
    eighth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1963 \nLondon, United Kingdom", color="black")
def ninth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1964"
    df = pd.read_html(url,match="Points")
    ninth = df[0]
    ninth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(ninth)
    ninth.Points = pd.to_numeric(ninth.Points)
    ninth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1964 \nCopenhagen, Denmark", color="black")
def tenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1965"
    df = pd.read_html(url,match="Points")
    tenth = df[0]
    tenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(tenth)
    tenth.Points = pd.to_numeric(tenth.Points)
    tenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1965 \nNaples, Italy", color="black")
def eleventh():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1966"
    df = pd.read_html(url,match="Points")
    eleventh = df[0]
    eleventh.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(eleventh)
    eleventh.Points = pd.to_numeric(eleventh.Points)
    eleventh.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1966 \nLuxembourg City, Luxembourg", color="black")
def twelfth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1967"
    df = pd.read_html(url,match="Points")
    twelfth = df[0]
    twelfth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twelfth)
    twelfth.Points = pd.to_numeric(twelfth.Points)
    twelfth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1967 \nVienna, Austria", color="black")
def thirteenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1968"
    df = pd.read_html(url,match="Points")
    thirteenth = df[0]
    thirteenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirteenth)
    thirteenth.Points = pd.to_numeric(thirteenth.Points)
    thirteenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1968 \nLondon, United Kingdom", color="black")
def fourteenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1969"
    df = pd.read_html(url,match="Points")
    fourteenth = df[0]
    fourteenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourteenth)
    fourteenth.Points = pd.to_numeric(fourteenth.Points)
    fourteenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1969 \nMadrid, Spain", color="black")
def fifteenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1970"
    df = pd.read_html(url,match="Points")
    fifteenth = df[0]
    fifteenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fifteenth)
    fifteenth.Points = pd.to_numeric(fifteenth.Points)
    fifteenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1970 \nAmsterdam, Netherlands", color="black")
    df = pd.read_html(url,match="Points")
def sixteenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1971"
    df = pd.read_html(url,match="Points")
    sixteenth = df[0]
    sixteenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixteenth)
    sixteenth.Points = pd.to_numeric(sixteenth.Points)
    sixteenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1971 \nDublin, Ireland", color="black")
def seventeenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1972"
    df = pd.read_html(url,match="Points")
    seventeenth = df[0]
    seventeenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(seventeenth)
    seventeenth.Points = pd.to_numeric(seventeenth.Points)
    seventeenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1972 \nEdinburgh, United Kingdom", color="black")
def eighteenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1973"
    df = pd.read_html(url,match="Points")
    eighteenth = df[0]
    eighteenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(eighteenth)
    eighteenth.Points = pd.to_numeric(eighteenth.Points)
    eighteenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1973 \nLuxembourg City, Luxembourg", color="black")
def nineteenth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1974"
    df = pd.read_html(url,match="Points")
    nineteenth = df[0]
    nineteenth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(nineteenth)
    nineteenth.Points = pd.to_numeric(nineteenth.Points)
    nineteenth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1974 \nBrighton, United Kingdom", color="black")
def twentieth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1975"
    df = pd.read_html(url,match="Points")
    twentieth = df[0]
    twentieth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentieth)
    twentieth.Points = pd.to_numeric(twentieth.Points)
    twentieth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1975 \nStockholm, Sweden", color="black")
def twentyfirst():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1976"
    df = pd.read_html(url,match="Points")
    twentyfirst = df[0]
    twentyfirst.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentyfirst)
    twentyfirst.Points = pd.to_numeric(twentyfirst.Points)
    twentyfirst.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1976 \nThe Hague, Netherlands", color="black")
def twentysecond():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1977"
    df = pd.read_html(url,match="Points")
    twentysecond = df[0]
    twentysecond.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentysecond)
    twentysecond.Points = pd.to_numeric(twentysecond.Points)
    twentysecond.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1977 \nLondon, United Kingdom", color="black")
def twentythird():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1978"
    df = pd.read_html(url,match="Points")
    twentythird = df[0]
    twentythird.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentythird)
    twentythird.Points = pd.to_numeric(twentythird.Points)
    twentythird.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1978 \nParis, France", color="black")
def twentyfourth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1979"
    df = pd.read_html(url,match="Points")
    twentyfourth = df[0]
    twentyfourth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentyfourth)
    twentyfourth.Points = pd.to_numeric(twentyfourth.Points)
    twentyfourth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1979 \nJerusalem, Israel", color="black")
def twentyfifth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1980"
    df = pd.read_html(url,match="Points")
    twentyfifth = df[0]
    twentyfifth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentyfifth)
    twentyfifth.Points = pd.to_numeric(twentyfifth.Points)
    twentyfifth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1980 \nThe Hague, Netherlands", color="black")
def twentysixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1981"
    df = pd.read_html(url,match="Points")
    twentysixth = df[0]
    twentysixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentysixth)
    twentysixth.Points = pd.to_numeric(twentysixth.Points)
    twentysixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1981 \nDublin, Ireland", color="black")
def twentyseventh():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1982"
    df = pd.read_html(url,match="Points")
    twentyseventh = df[0]
    twentyseventh.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentyseventh)
    twentyseventh.Points = pd.to_numeric(twentyseventh.Points)
    twentyseventh.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1982 \nHarrogate, United Kingdom", color="black")
def twentyeighth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1983"
    df = pd.read_html(url,match="Points")
    twentyeighth = df[0]
    twentyeighth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentyeighth)
    twentyeighth.Points = pd.to_numeric(twentyeighth.Points)
    twentyeighth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1983 \nMunich, West Germany", color="black")
def twentyninth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1984"
    df = pd.read_html(url,match="Points")
    twentyninth = df[0]
    twentyninth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(twentyninth)
    twentyninth.Points = pd.to_numeric(twentyninth.Points)
    twentyninth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1984 \nLuxembourg City, Luxembourg", color="black")
def thirtieth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1985"
    df = pd.read_html(url,match="Points")
    thirtieth = df[0]
    thirtieth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtieth)
    thirtieth.Points = pd.to_numeric(thirtieth.Points)
    thirtieth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1985 \nGothenburg, Sweden", color="black")
def thirtyfirst():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1986"
    df = pd.read_html(url,match="Points")
    thirtyfirst = df[0]
    thirtyfirst.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyfirst)
    thirtyfirst.Points = pd.to_numeric(thirtyfirst.Points)
    thirtyfirst.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1986 \nBergen, Norway", color="black")
def thirtysecond():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1987"
    df = pd.read_html(url,match="Points")
    thirtysecond = df[0]
    thirtysecond.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtysecond)
    thirtysecond.Points = pd.to_numeric(thirtysecond.Points)
    thirtysecond.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1987 \nBrussels, Belgium", color="black")
def thirtythird():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1988"
    df = pd.read_html(url,match="Points")
    thirtythird = df[0]
    thirtythird.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtythird)
    thirtythird.Points = pd.to_numeric(thirtythird.Points)
    thirtythird.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1988 \nDublin, Ireland", color="black")
def thirtyfourth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1989"
    df = pd.read_html(url,match="Points")
    thirtyfourth = df[0]
    thirtyfourth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyfourth)
    thirtyfourth.Points = pd.to_numeric(thirtyfourth.Points)
    thirtyfourth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1989 \nLausanne, Switzerland", color="black")
def thirtyfifth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1990"
    df = pd.read_html(url,match="Points")
    thirtyfifth = df[0]
    thirtyfifth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyfifth)
    thirtyfifth.Points = pd.to_numeric(thirtyfifth.Points)
    thirtyfifth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1990 \nZagreb, Yugoslavia", color="black")
def thirtysixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1991"
    df = pd.read_html(url,match="Points")
    thirtysixth = df[0]
    thirtysixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtysixth)
    thirtysixth.Points = pd.to_numeric(thirtysixth.Points)
    thirtysixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1991 \nRome, Italy", color="black")
def thirtyseventh():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1992"
    df = pd.read_html(url,match="Points")
    thirtyseventh = df[0]
    thirtyseventh.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyseventh)
    thirtyseventh.Points = pd.to_numeric(thirtyseventh.Points)
    thirtyseventh.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1992 \nMalmo, Sweden", color="black")
def thirtyeighthsemi():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Kvalifikacija_za_Millstreet"
    df = pd.read_html(url,match="Points")
    thirtyeighthsemi = df[0]
    thirtyeighthsemi.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyeighthsemi)
    thirtyeighthsemi.Points = pd.to_numeric(thirtyeighthsemi.Points)
    thirtyeighthsemi.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Kvalifikacija za Millstreet 1993 \nLjubljana, Slovenia", color="black")
def thirtyeighth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1993"
    df = pd.read_html(url,match="Points")
    thirtyeighth = df[0]
    thirtyeighth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyeighth)
    thirtyeighth.Points = pd.to_numeric(thirtyeighth.Points)
    thirtyeighth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision 1993 \nMillstreet, Ireland", color="black")
def thirtyninth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1994"
    df = pd.read_html(url,match="Points")
    thirtyninth = df[0]
    thirtyninth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(thirtyninth)
    thirtyninth.Points = pd.to_numeric(thirtyninth.Points)
    thirtyninth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1994 \nDublin, Ireland", color="black")
def fourteith():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1995"
    df = pd.read_html(url,match="Points")
    fourtieth = df[0]
    fourtieth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtieth)
    fourtieth.Points = pd.to_numeric(fourtieth.Points)
    fourtieth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1995 \nDublin, Ireland", color="black")
def fourtyfirstsemi():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1996"
    df = pd.read_html(url,match="Points")
    fourtyfirstsemi = df[0]
    fourtyfirstsemi.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyfirstsemi)
    fourtyfirstsemi.Points = pd.to_numeric(fourtyfirstsemi.Points)
    fourtyfirstsemi.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1996 \nSemi-Final \nOslo, Norway", color="black")
def fourtyfirst():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1996"
    df = pd.read_html(url,match="Points")
    fourtyfirst = df[1]
    fourtyfirst.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyfirst)
    fourtyfirst.Points = pd.to_numeric(fourtyfirst.Points)
    fourtyfirst.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1996 \nOslo, Norway", color="black")
def fourtysecond():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1997"
    df = pd.read_html(url,match="Points")
    fourtysecond = df[0]
    fourtysecond.columns = ['Running Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtysecond)
    fourtysecond.Points = pd.to_numeric(fourtysecond.Points)
    fourtysecond.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1997 \nDublin, Ireland", color="black")
def fourtythird():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1998"
    df = pd.read_html(url,match="Points")
    fourtythird = df[0]
    fourtythird.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtythird)
    fourtythird.Points = pd.to_numeric(fourtythird.Points)
    fourtythird.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1998 \nBirmingham, United Kingdom", color="black")
def fourtyfourth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_1999"
    df = pd.read_html(url,match="Points")
    fourtyfourth = df[0]
    fourtyfourth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyfourth)
    fourtyfourth.Points = pd.to_numeric(fourtyfourth.Points)
    fourtyfourth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 1999 \nJerusalem, Israel", color="black")
def fourtyfifth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2000"
    df = pd.read_html(url,match="Points")
    fourtyfifth = df[0]
    fourtyfifth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyfifth)
    fourtyfifth.Points = pd.to_numeric(fourtyfifth.Points)
    fourtyfifth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2000 \nStockholm, Sweden", color="black")
def fourtysixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2001"
    df = pd.read_html(url,match="Points")
    fourtysixth = df[0]
    fourtysixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtysixth)
    fourtysixth.Points = pd.to_numeric(fourtysixth.Points)
    fourtysixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2001 \nCopenhagen, Denmark", color="black")
def fourtyseventh():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2002"
    df = pd.read_html(url,match="Points")
    fourtyseventh = df[0]
    fourtyseventh.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyseventh)
    fourtyseventh.Points = pd.to_numeric(fourtyseventh.Points)
    fourtyseventh.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2002 \nTallinn, Estonia", color="black")
def fourtyeighth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2003"
    df = pd.read_html(url,match="Points")
    fourtyeighth = df[0]
    fourtyeighth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyeighth)
    fourtyeighth.Points = pd.to_numeric(fourtyeighth.Points)
    fourtyeighth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2003 \nSemi-Final \nRiga, Latvia", color="black")
def fourtyninthsemi():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2004"
    df = pd.read_html(url,match="Points")
    fourtyninthsemi = df[0]
    fourtyninthsemi.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyninthsemi)
    fourtyninthsemi.Points = pd.to_numeric(fourtyninthsemi.Points)
    fourtyninthsemi.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2004 \nSemi-Final \nIstanbul, Turkey", color="black")
def fourtyninth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2004"
    df = pd.read_html(url,match="Points")
    fourtyninth = df[1]
    fourtyninth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fourtyninth)
    fourtyninth.Points = pd.to_numeric(fourtyninth.Points)
    fourtyninth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2004 \nGrand Final \nIstanbul, Turkey", color="black")
def fiftiethsemi():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2005"
    df = pd.read_html(url,match="Points")
    fiftiethsemi = df[0]
    fiftiethsemi.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftiethsemi)
    fiftiethsemiPoints = pd.to_numeric(fiftiethsemi.Points)
    fiftiethsemi.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2005 \nSemi-Final \nKyiv, Ukraine", color="black")
def fiftieth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2005"
    df = pd.read_html(url,match="Points")
    fiftieth = df[1]
    fiftieth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftieth)
    fiftieth.Points = pd.to_numeric(fiftieth.Points)
    fiftieth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2005 \nKyiv, Ukraine", color="black")
def fiftyfirstsemi():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2006"
    df = pd.read_html(url,match="Points")
    fiftyfirstsemi = df[0]
    fiftyfirstsemi.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfirstsemi)
    fiftyfirstsemi.Points = pd.to_numeric(fiftyfirstsemi.Points)
    fiftyfirstsemi.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2006 \nSemi-Final \nAthens, Greece", color="black")
def fiftyfirst():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2006"
    df = pd.read_html(url,match="Points")
    fiftyfirst = df[1]
    fiftyfirst.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfirst)
    fiftyfirst.Points = pd.to_numeric(fiftyfirst.Points)
    fiftyfirst.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2006 \nAthens, Greece", color="black")
def fiftysecondsemi():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2007"
    df = pd.read_html(url,match="Points")
    fiftysecondsemi = df[0]
    fiftysecondsemi.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftysecondsemi)
    fiftysecondsemi.Points = pd.to_numeric(fiftysecondsemi.Points)
    fiftysecondsemi.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2007 \nSemi-Final \nHelsinki, Finland", color="black")
def fiftysecond():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2007"
    df = pd.read_html(url,match="Points")
    fiftysecond = df[1]
    fiftysecond.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftysecond)
    fiftysecond.Points = pd.to_numeric(fiftysecond.Points)
    fiftysecond.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2007 \nGrand Final \nHelsinki, Finland", color="black")
def fiftythirdsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2008"
    df = pd.read_html(url,match="Points")
    fiftythirdsemione = df[0]
    fiftythirdsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftythirdsemione)
    fiftythirdsemione.Points = pd.to_numeric(fiftythirdsemione.Points)
    fiftythirdsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2008 \nSemi-Final One \nBelgrade, Serbia", color="black")
def fiftythirdsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2008"
    df = pd.read_html(url,match="Points")
    fiftythirdsemitwo = df[1]
    fiftythirdsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftythirdsemitwo)
    fiftythirdsemitwo.Points = pd.to_numeric(fiftythirdsemitwo.Points)
    fiftythirdsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2008 \nSemi-Final Two\nBelgrade, Serbia", color="black")
def fiftythird():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2008"
    df = pd.read_html(url,match="Points")
    fiftythird = df[2]
    fiftythird.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftythird)
    fiftythird.Points = pd.to_numeric(fiftythird.Points)
    fiftythird.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2008 \nGrand Final \nBelgrade, Serbia", color="black")
def fiftyfourthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2009"
    df = pd.read_html(url,match="Points")
    fiftyfourthsemione = df[0]
    fiftyfourthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfourthsemione)
    fiftyfourthsemione.Points = pd.to_numeric(fiftyfourthsemione.Points)
    fiftyfourthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2009 \nSemi-Final One \nMoscow, Russia", color="black")
def fiftyfourthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2009"
    df = pd.read_html(url,match="Points")
    fiftyfourthsemitwo = df[1]
    fiftyfourthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfourthsemitwo)
    fiftyfourthsemitwo.Points = pd.to_numeric(fiftyfourthsemitwo.Points)
    fiftyfourthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2009 \nSemi-Final Two \nMoscow, Russia", color="black")
def fiftyfourth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2009"
    df = pd.read_html(url,match="Points")
    fiftyfourth = df[2]
    fiftyfourth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfourth)
    fiftyfourth.Points = pd.to_numeric(fiftyfourth.Points)
    fiftyfourth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2009 \nGrand Final \nMoscow, Russia", color="black")
def fiftyfifthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2010"
    df = pd.read_html(url,match="Points")
    fiftyfifthsemione = df[0]
    fiftyfifthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfifthsemione)
    fiftyfifthsemione.Points = pd.to_numeric(fiftyfifthsemione.Points)
    fiftyfifthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2010 \nSemi-Final One \nOslo, Norway", color="black")
def fiftyfifthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2010"
    df = pd.read_html(url,match="Points")
    fiftyfifthsemitwo = df[1]
    fiftyfifthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfifthsemitwo)
    fiftyfifthsemitwo.Points = pd.to_numeric(fiftyfifthsemitwo.Points)
    fiftyfifthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2010 \nSemi-Final Two \nOslo, Norway", color="black")
def fiftyfifth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2010"
    df = pd.read_html(url,match="Points")
    fiftyfifth = df[2]
    fiftyfifth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyfifth)
    fiftyfifth.Points = pd.to_numeric(fiftyfifth.Points)
    fiftyfifth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2010 \nGrand Final \nOslo, Norway", color="black")
def fiftysixthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2011"
    df = pd.read_html(url,match="Points")
    fiftysixthsemione = df[0]
    fiftysixthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftysixthsemione)
    fiftysixthsemione.Points = pd.to_numeric(fiftysixthsemione.Points)
    fiftysixthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2011 \nSemi-Final One \nDusseldorf, Germany", color="black")
def fiftysixthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2011"
    df = pd.read_html(url,match="Points")
    fiftysixthsemitwo = df[1]
    fiftysixthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftysixthsemitwo)
    fiftysixthsemitwo.Points = pd.to_numeric(fiftysixthsemitwo.Points)
    fiftysixthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2011 \nSemi-Final Two \nDusseldorf, Germany", color="black")
def fiftysixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2011"
    df = pd.read_html(url,match="Points")
    fiftysixth = df[2]
    fiftysixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftysixth)
    fiftysixth.Points = pd.to_numeric(fiftysixth.Points)
    fiftysixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2011 \nGrand Final \nDusseldorf, Germany", color="black")
def fiftysixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2011"
    df = pd.read_html(url,match="Points")
    fiftysixth = df[2]
    fiftysixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftysixth)
    fiftysixth.Points = pd.to_numeric(fiftysixth.Points)
    fiftysixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2011 \nGrand Final \nDusseldorf, Germany", color="black")
def fiftyseventhsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2012"
    df = pd.read_html(url,match="Points")
    fiftyseventhsemione = df[0]
    fiftyseventhsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyseventhsemione)
    fiftyseventhsemione.Points = pd.to_numeric(fiftyseventhsemione.Points)
    fiftyseventhsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2012 \nSemi-Final One \nBaku, Azerbaijan", color="black")
def fiftyseventhsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2012"
    df = pd.read_html(url,match="Points")
    fiftyseventhsemitwo = df[1]
    fiftyseventhsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyseventhsemitwo)
    fiftyseventhsemitwo.Points = pd.to_numeric(fiftyseventhsemitwo.Points)
    fiftyseventhsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2012 \nSemi-Final Two \nBaku, Azerbaijan", color="black")
def fiftyseventh():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2012"
    df = pd.read_html(url,match="Points")
    fiftyseventh = df[2]
    fiftyseventh.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyseventh)
    fiftyseventh.Points = pd.to_numeric(fiftyseventh.Points)
    fiftyseventh.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2012 \nGrand Final \nBaku, Azerbaijan", color="black")
def fiftyeighthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2013"
    df = pd.read_html(url,match="Points")
    fiftyeighthsemione = df[0]
    fiftyeighthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyeighthsemione)
    fiftyeighthsemione.Points = pd.to_numeric(fiftyeighthsemione.Points)
    fiftyeighthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2013 \nSemi-Final One \nMalmo, Sweden", color="black")
def fiftyeighthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2013"
    df = pd.read_html(url,match="Points")
    fiftyeighthsemitwo = df[1]
    fiftyeighthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyeighthsemitwo)
    fiftyeighthsemitwo.Points = pd.to_numeric(fiftyeighthsemitwo.Points)
    fiftyeighthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2013 \nSemi-Final Two \nMalmo, Sweden", color="black")
def fiftyeighth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2013"
    df = pd.read_html(url,match="Points")
    fiftyeighth = df[2]
    fiftyeighth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyeighth)
    fiftyeighth.Points = pd.to_numeric(fiftyeighth.Points)
    fiftyeighth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2013 \nGrand Final \nMalmo, Sweden", color="black")
def fiftyninthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2014"
    df = pd.read_html(url,match="Points")
    fiftyninthsemione = df[0]
    fiftyninthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyninthsemione)
    fiftyninthsemione.Points = pd.to_numeric(fiftyninthsemione.Points)
    fiftyninthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2014 \nSemi-Final One \nCopenhagen, Denmark", color="black")
def fiftyninthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2014"
    df = pd.read_html(url,match="Points")
    fiftyninthsemitwo = df[1]
    fiftyninthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyninthsemitwo)
    fiftyninthsemitwo.Points = pd.to_numeric(fiftyninthsemitwo.Points)
    fiftyninthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2014 \nSemi-Final Two \nCopenhagen, Denmark", color="black")
def fiftyninth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2014"
    df = pd.read_html(url,match="Points")
    fiftyninth = df[2]
    fiftyninth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(fiftyninth)
    fiftyninth.Points = pd.to_numeric(fiftyninth.Points)
    fiftyninth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2014 \nGrand Final \nCopenhagen, Denmark", color="black")
def sixtiethsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2015"
    df = pd.read_html(url,match="Points")
    sixtiethsemione = df[0]
    sixtiethsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtiethsemione)
    sixtiethsemione.Points = pd.to_numeric(sixtiethsemione.Points)
    sixtiethsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2015 \nSemi-Final One \nVienna, Austria", color="black")
def sixtiethsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2015"
    df = pd.read_html(url,match="Points")
    sixtiethsemitwo = df[1]
    sixtiethsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtiethsemitwo)
    sixtiethsemitwo.Points = pd.to_numeric(sixtiethsemitwo.Points)
    sixtiethsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2015 \nSemi-Final Two \nVienna, Austria", color="black")
def sixtieth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2015"
    df = pd.read_html(url,match="Points")
    sixtieth = df[2]
    sixtieth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtieth)
    sixtieth.Points = pd.to_numeric(sixtieth.Points)
    sixtieth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2015 \nGrand Final \nVienna, Austria", color="black")
def sixtyfirstsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2016"
    df = pd.read_html(url,match="Points")
    sixtyfirstsemione = df[0]
    sixtyfirstsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfirstsemione)
    sixtyfirstsemione.Points = pd.to_numeric(sixtyfirstsemione.Points)
    sixtyfirstsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2016 \nSemi-Final One \nStockholm, Sweden", color="black")
def sixtyfirstsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2016"
    df = pd.read_html(url,match="Points")
    sixtyfirstsemitwo = df[1]
    sixtyfirstsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfirstsemitwo)
    sixtyfirstsemitwo.Points = pd.to_numeric(sixtyfirstsemitwo.Points)
    sixtyfirstsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2016 \nSemi-Final Two \nStockholm, Sweden", color="black")
def sixtyfirst():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2016"
    df = pd.read_html(url,match="Points")
    sixtyfirst = df[2]
    sixtyfirst.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfirst)
    sixtyfirst.Points = pd.to_numeric(sixtyfirst.Points)
    sixtyfirst.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2016 \nGrand Final \nStockholm, Sweden", color="black")
def sixtysecondsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2017"
    df = pd.read_html(url,match="Points")
    sixtysecondsemione = df[0]
    sixtysecondsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtysecondsemione)
    sixtysecondsemione.Points = pd.to_numeric(sixtysecondsemione.Points)
    sixtysecondsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2016 \nSemi-Final One \nKyiv, Ukraine", color="black")
def sixtysecondsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2017"
    df = pd.read_html(url,match="Points")
    sixtysecondsemitwo = df[1]
    sixtysecondsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtysecondsemitwo)
    sixtysecondsemitwo.Points = pd.to_numeric(sixtysecondsemitwo.Points)
    sixtysecondsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2016 \nSemi-Final Two \nKyiv, Ukraine", color="black")
def sixtysecond():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2017"
    df = pd.read_html(url,match="Points")
    sixtysecond = df[2]
    sixtysecond.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtysecond)
    sixtysecond.Points = pd.to_numeric(sixtysecond.Points)
    sixtysecond.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2016 \nGrand Final \nKyiv, Ukraine", color="black")
def sixtythirdsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2018"
    df = pd.read_html(url,match="Points")
    sixtythirdsemione = df[0]
    sixtythirdsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtythirdsemione)
    sixtythirdsemione.Points = pd.to_numeric(sixtythirdsemione.Points)
    sixtythirdsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2018 \nSemi-Final One \nLisbon, Portugal", color="black")
def sixtythirdsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2018"
    df = pd.read_html(url,match="Points")
    sixtythirdsemitwo = df[1]
    sixtythirdsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtythirdsemitwo)
    sixtythirdsemitwo.Points = pd.to_numeric(sixtythirdsemitwo.Points)
    sixtythirdsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2018 \nSemi-Final Two \nLisbon, Portugal", color="black")
def sixtythird():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2018"
    df = pd.read_html(url,match="Points")
    sixtythird = df[2]
    sixtythird.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtythird)
    sixtythird.Points = pd.to_numeric(sixtythird.Points)
    sixtythird.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2018 \nGrand Final \nLisbon, Portugal", color="black")
def sixtyfourthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2019"
    df = pd.read_html(url,match="Points")
    sixtyfourthsemione = df[0]
    sixtyfourthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfourthsemione)
    sixtyfourthsemione.Points = pd.to_numeric(sixtyfourthsemione.Points)
    sixtyfourthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2019 \nSemi-Final One \nTel Aviv, Israel", color="black")
def sixtyfourthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2019"
    df = pd.read_html(url,match="Points")
    sixtyfourthsemitwo = df[1]
    sixtyfourthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfourthsemitwo)
    sixtyfourthsemitwo.Points = pd.to_numeric(sixtyfourthsemitwo.Points)
    sixtyfourthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2019 \nSemi-Final Two \nTel Aviv, Israel", color="black")
def sixtyfourth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2019"
    df = pd.read_html(url,match="Points")
    sixtyfourth = df[2]
    sixtyfourth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfourth)
    sixtyfourth.Points = pd.to_numeric(sixtyfourth.Points)
    sixtyfourth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2019 \nGrand Final \nTel Aviv, Israel", color="black")
def sixtyfifthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2021"
    df = pd.read_html(url,match="Points")
    sixtyfifthsemione = df[0]
    sixtyfifthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfifthsemione)
    sixtyfifthsemione.Points = pd.to_numeric(sixtyfifthsemione.Points)
    sixtyfifthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2021 \nSemi-Final One \nRotterdam, Netherlands", color="black")
def sixtyfifthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2021"
    df = pd.read_html(url,match="Points")
    sixtyfifthsemitwo = df[1]
    sixtyfifthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfifthsemitwo)
    sixtyfifthsemitwo.Points = pd.to_numeric(sixtyfifthsemitwo.Points)
    sixtyfifthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2021 \nSemi-Final Two \nRotterdam, Netherlands", color="black")
def sixtyfifth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2021"
    df = pd.read_html(url,match="Points")
    sixtyfifth = df[2]
    sixtyfifth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtyfifth)
    sixtyfifth.Points = pd.to_numeric(sixtyfifth.Points)
    sixtyfifth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2021 \nGrand Final \nRotterdam, Netherlands", color="black")
def sixtysixthsemione():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2022"
    df = pd.read_html(url,match="Points")
    sixtysixthsemione = df[0]
    sixtysixthsemione.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtysixthsemione)
    sixtysixthsemione.Points = pd.to_numeric(sixtysixthsemione.Points)
    sixtysixthsemione.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2022 \nSemi-Final One \nTurin, Italy", color="black")
def sixtysixthsemitwo():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2022"
    df = pd.read_html(url,match="Points")
    sixtysixthsemitwo = df[1]
    sixtysixthsemitwo.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtysixthsemitwo)
    sixtysixthsemitwo.Points = pd.to_numeric(sixtysixthsemitwo.Points)
    sixtysixthsemitwo.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2022 \nSemi-Final Two \nTurin, Italy", color="black")
def sixtysixth():
    import pandas as pd
    url="https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2022"
    df = pd.read_html(url,match="Points")
    sixtysixth = df[2]
    sixtysixth.columns = ['Order', 'Country', 'Artist', 'Song', 'Language', 'Points', 'Place']
    display(sixtysixth)
    sixtysixth.Points = pd.to_numeric(sixtysixth.Points)
    sixtysixth.plot.bar(x='Country', y='Points', xlabel="Country", ylabel="Points", title="Eurovision Song Contest 2022 \nGrand Final \nTurin, Italy", color="black")
    
# Menu
# supporting functions called from main menu

def intro():
    print("Hello! I the Eurovision Information bot and am here to help you learn about the most watched annual television program in the world, the Eurovision Song Contest!")
    import time
    time.sleep(1)
    print("While I thank you for your interest in the Eurovision Song Contest, I don't know your name yet! Could you please share?")
    name = input()
    time.sleep(1)
    print("Thanks " + name + ", could you share what country you are from please.")
    country = input()
    time.sleep(1)
    print("Thank you")
    if "States" in country:
      print("The United States has the American Song Contest, which premiered on NBC in 2022 with AleXa from Oklahoma winning.")
    if "states" in country:
      print("The United States has the American Song Contest, which premiered on NBC in 2022 with AleXa from Oklahoma winning.")
    if "Kingdom" in country:
      print("The United Kingdom has won the contest numerous times and is hosting the 2023 edition.")
    time.sleep(1)
    heard = input("Have you ever heard of the Eurovision Song Contest?")
    if "Yes" in heard:
      print("Wonderful, then you already know the contest takes place in Europe and began in 1956.")
    if "No" in heard:
      print("The Eurovision Song Contest started in 1956 to bring post war Europe together.")
    if "yes" in heard:
      print("Wonderful, then you already know the contest takes place in Europe and began in 1956.")
    if "no" in heard:
      print("The Eurovision Song Contest started in 1956 to bring post war Europe together.")
    else:
      print("Get ready to learn all about it.")
    print("In Eurovision, countries from across Europe, sometimes up to 43 countries, send a song to represent their nation in a song contest that is viewed across the world.")
    print("The results are tabulated according to a professional jury of music professionals from each country and a televote from the viewers at home.")
    print("Some contests have semifinals where only ten songs will qualify to the final.")
    print("Several countries are prequalified to the final because of the money they give the European Broadcasting Union. They are France, Germany, Italy, and the United Kingdom. The host country automatically qualifies as well.")
    print("Once a contest is won, then that country has the opportunity to host the contest the next year.")
    menu()

def news():
    from GoogleNews import GoogleNews
    news=GoogleNews(period='1D')
    news.search("Eurovision Song Contest")
    result = news.result()
    import pandas as pd
    data = pd.DataFrame.from_dict(result)
    data.head()
    for i in result:
        print("Title : ", i["title"])
        print("News :", i["desc"])
        print("Read Full News :", i["link"])
    menu()
    
def first_contest():
    print("******1956 Contest Menu******")
    import time
    time.sleep(1)
    choice = input("""
            A: Interesting Info
            B: Grand Final
    """)
    if choice == "A" or "a":
        print("The 1956 contest was hosted in Lugano, Switzerland.")
        print("Grand Prix Eurovision de la Chanson Européenne 1956 was the original name.")
        print("It took place at the Teatro Kursaal and was hosted by Lohengrin Filipello.")
        print("This is to date the only time Switzerland has ever hosted.")
    elif choice == "B" or "b":
        print("Lys Assia won with the song 'Refrain' in French")
        print("It is assumed that West Germany won, as they hosted the next year, though second through fourteenth place was never revealed.")
# contest menu
def contests_menu():
    import time
    print("******Eurovision Song Contest Year Menu******")
    time.sleep(1)
    choice = input("""
            Type any year from 1956 to 2023.
    """)
    if choice == "1956":
        first_contest()
    elif choice == "1957":
        second()
    elif choice == "1958":
        third()
    elif choice == "1959":
        fourth()
    elif choice == "1960":
        fifth()
    elif choice == "1961":
        sixth()
    elif choice == "1962":
        seventh()
    elif choice == "1963":
        eighth()
    elif choice == "1964":
        ninth()
    elif choice == "1965":
        tenth()
    elif choice == "1966":
        eleventh()
    elif choice == "1967":
        twelfth()
    elif choice == "1968":
        thirteenth()
    elif choice == "1969":
        fourteenth()
    elif choice == "1970":
        fifteenth()
    elif choice == "1971":
        sixteenth()
    elif choice == "1972":
        seventeenth()
    elif choice == "1973":
        eighteenth()
    elif choice == "1974":
        nineteenth()
    elif choice == "1975":
        twentieth()
    elif choice == "1976":
        twentyfirst()
    elif choice == "1977":
        twentysecond()
    elif choice == "1978":
        twentythird()
    elif choice == "1979":
        twentyfourth()
    elif choice == "1980":
        twentyfifth()
    elif choice == "1981":
        twentysixth()
    elif choice == "1982":
        twentyseventh()
    elif choice == "1983":
        twentyeighth()
    elif choice == "1984":
        twentyninth()
    elif choice == "1985":
        thirtieth()
    elif choice == "1986":
        thirtyfirst()
    elif choice == "1987":
        thirtysecond()
    elif choice == "1988":
        thirtythird()
    elif choice == "1989":
        thirtyfourth()
    elif choice == "1990":
        thirtyfifth()
    elif choice == "1991":
        thirtysixth()
    elif choice == "1992":
        thirtyseventh()
    elif choice == "1993":
        thirtyeighthsemi()
        thirtyeighth()
    elif choice == "1994":
        thirtyninth()
    elif choice == "1995":
        fourteith()
    elif choice == "1996":
        print("******Semi Final******")
        fourtyfirstsemi()
        print("******Grand Final******")
        fourtyfirst()
    elif choice == "1997":
        fourtysecond()
    elif choice == "1998":
        fourtythird()
    elif choice == "1999":
        fourtyfourth()
    elif choice == "2000":
        fourtyfifth()
    elif choice == "2001":
        fourtysixth()
    elif choice == "2002":
        fourtyseventh()
    elif choice == "2003":
        fourtyeighth()
    elif choice == "2004":
        print("******Semi Final******")
        fourtyninthsemi()
        print("******Grand Final******")
        fourtyninth()
    elif choice == "2005":
        print("******Semi Final******")
        fiftiethsemi()
        print("******Grand Final******")
        fiftieth()
    elif choice == "2006":
        print("******Semi Final******")
        fiftyfirstsemi()
        print("******Grand Final******")
        fiftyfirst()
    elif choice == "2007":
        print("******Semi Final******")
        fiftysecondsemi()
        print("******Grand Final******")
        fiftysecond()
    elif choice == "2008":
        print("******Semi Final One******")
        fiftythirdsemione()
        print("******Semi Final Two******")
        fiftythirdsemitwo()
        print("******Grand Final******")
        fiftythird()
    elif choice == "2009":
        print("******Semi Final One******")
        fiftyfourthsemione()
        print("******Semi Final Two******")
        fiftyfourthsemitwo()
        print("******Grand Final******")
        fiftyfourth()
    elif choice == "2010":
        print("******Semi Final One******")
        fiftyfifthsemione()
        print("******Semi Final Two******")
        fiftyfifthsemitwo()
        print("******Grand Final******")
        fiftyfifth()
    elif choice == "2011":
        print("******Semi Final One******")
        fiftysixthsemione()
        print("******Semi Final Two******")
        fiftysixthsemitwo()
        print("******Grand Final******")
        fiftysixth()
    elif choice == "2012":
        print("******Semi Final One******")
        fiftyseventhsemione()
        print("******Semi Final Two******")
        fiftyseventhsemitwo()
        print("******Grand Final******")
        fiftyseventh()
    elif choice == "2013":
        print("******Semi Final One******")
        fiftyeighthsemione()
        print("******Semi Final Two******")
        fiftyeighthsemitwo()
        print("******Grand Final******")
        fiftyeighth()
    elif choice == "2014":
        print("******Semi Final One******")
        fiftyninthsemione()
        print("******Semi Final Two******")
        fiftyninthsemitwo()
        print("******Grand Final******")
        fiftyninth()
    elif choice == "2015":
        print("******Semi Final One******")
        sixtiethsemione()
        print("******Semi Final Two******")
        sixtiethsemitwo()
        print("******Grand Final******")
        sixtieth()
    elif choice == "2016":
        print("******Semi Final One******")
        sixtyfirstsemione()
        print("******Semi Final Two******")
        sixtyfirstsemitwo()
        print("******Grand Final******")
        sixtyfirst()
    elif choice == "2017":
        print("******Semi Final One******")
        sixtysecondsemione()
        print("******Semi Final Two******")
        sixtysecondsemitwo()
        print("******Grand Final******")
        sixtysecond()
    elif choice == "2018":
        print("******Semi Final One******")
        sixtythirdsemione()
        print("******Semi Final Two******")
        sixtythirdsemitwo()
        print("******Grand Final******")
        sixtythird()
    elif choice == "2019":
        print("******Semi Final One******")
        sixtyfourthsemione()
        print("******Semi Final Two******")
        sixtyfourthsemitwo()
        print("******Grand Final******")
        sixtyfourth()
    elif choice == "2020":
        print("This contest was canceled due to the COVID-19 pandemic.")
    elif choice == "2021":
        print("******Semi Final One******")
        sixtyfifthsemione()
        print("******Semi Final Two******")
        sixtyfifthsemitwo()
        print("******Grand Final******")
        sixtyfifth()
    elif choice == "2022":
        print("******Semi Final One******")
        sixtysixthsemione()
        print("******Semi Final Two******")
        sixtysixthsemitwo()
        print("******Grand Final******")
        sixtysixth()
    elif choice == "2023":
        print("The 66th contest is set to be held in Liverpool, United Kingdom after Ukraine won in 2022 but can't host due to the Russian invasion.")
    elif choice == "Q" or choice == "q":
        quit()
    elif choice == "M" or choice == "m":
        menu()
    else:
        print("Oops, I can't seem to find the Wikipedia article for that year. Try again or type M to go to the main menu or Q to quit.")
        contests_menu()
def menu():
    print("******Main Menu******")
    import time
    time.sleep(1)
    choice = input("""
            A: Start here.
            B: Individual contests info.
            C: News on upcoming contests.
            Q: Quit.     
        
            Please choose a lettered choice.
    """)
    if choice == "A" or choice == "a":
        intro()
    elif choice == "B" or choice == "b":
        contests_menu()
    elif choice == "C" or choice == "c":
        news()
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("Oops, try again please...")
        menu()
