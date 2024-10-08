import pandas as pd

# Manually selected representative songs for each era
data = {
    "Song Title": [
        # Old School (1979–1983)
        "Rapper's Delight", "The Breaks", "The Message", "Planet Rock", "Apache", 
        "Sucker M.C.'s", "White Lines (Don't Do It)", "Rockin' It", "Funky 4 + 1", "It's Like That",
        
        # Golden Age (1983–1997)
        "Fight the Power", "Nuthin' But a G Thang", "Juicy", "C.R.E.A.M.", "Straight Outta Compton", 
        "The Low End Theory", "Paid in Full", "Me, Myself and I", "My Adidas", "Ain't No Half Steppin'",
        
        # East vs. West (1991–1997)
        "California Love", "Hypnotize", "Gin and Juice", "Dear Mama", "It Was a Good Day",
        "Who Shot Ya?", "Hit 'Em Up", "N.Y. State of Mind", "Ready to Die", "All Eyez on Me",

        # Rise of Southern Rap (1990–2005)
        "Mind Playing Tricks on Me", "Ridin' Dirty", "Southernplayalisticadillacmuzik", "Back That Azz Up", "Big Pimpin'",
        "Tha Block Is Hot", "What You Know", "Get Low", "Ms. Jackson", "Still Tippin'",

        # Bling Era (1997–2006)
        "In Da Club", "Hot in Herre", "Yeah!", "The Way I Am", "99 Problems", 
        "Go DJ", "Gold Digger", "Grillz", "Get Ur Freak On", "Rosa Parks",

        # Conscious Resurgence (2004–present)
        "Alright", "Jesus Walks", "Be", "The Story of O.J.", "Swimming Pools (Drank)",
        "DNA.", "Mortal Man", "Black America Again", "Power", "Runaway",

        # Blog Era & Trap (2006–present)
        "Sicko Mode", "Bodak Yellow", "Mask Off", "XO TOUR Llif3", "HUMBLE.", 
        "Drip Too Hard", "Hotline Bling", "God's Plan", "Lucid Dreams", "Old Town Road"
    ],
    "Artist": [
        # Old School
        "Sugarhill Gang", "Kurtis Blow", "Grandmaster Flash", "Afrika Bambaataa", "The Incredible Bongo Band", 
        "Run-D.M.C.", "Grandmaster Flash", "Fearless Four", "Funky 4 + 1", "Run-D.M.C.",
        
        # Golden Age
        "Public Enemy", "Dr. Dre", "The Notorious B.I.G.", "Wu-Tang Clan", "N.W.A.", 
        "A Tribe Called Quest", "Eric B. & Rakim", "De La Soul", "Run-D.M.C.", "Big Daddy Kane",
        
        # East vs. West
        "2Pac ft. Dr. Dre", "The Notorious B.I.G.", "Snoop Dogg", "2Pac", "Ice Cube",
        "The Notorious B.I.G.", "2Pac", "Nas", "The Notorious B.I.G.", "2Pac",

        # Rise of Southern Rap
        "Geto Boys", "UGK", "OutKast", "Juvenile", "Jay-Z ft. UGK",
        "Lil Wayne", "T.I.", "Lil Jon", "OutKast", "Mike Jones",

        # Bling Era
        "50 Cent", "Nelly", "Usher ft. Lil Jon", "Eminem", "Jay-Z", 
        "Lil Wayne", "Kanye West", "Nelly ft. Paul Wall", "Missy Elliott", "OutKast",

        # Conscious Resurgence
        "Kendrick Lamar", "Kanye West", "Common", "Jay-Z", "Kendrick Lamar",
        "Kendrick Lamar", "Kendrick Lamar", "Common", "Kanye West", "Kanye West",

        # Blog Era & Trap
        "Travis Scott", "Cardi B", "Future", "Lil Uzi Vert", "Kendrick Lamar", 
        "Lil Baby & Gunna", "Drake", "Drake", "Juice WRLD", "Lil Nas X"
    ],
    "Year": [
        # Old School
        1979, 1980, 1982, 1982, 1981, 
        1983, 1983, 1984, 1980, 1983,
        
        # Golden Age
        1989, 1992, 1994, 1993, 1988, 
        1991, 1987, 1989, 1986, 1988,
        
        # East vs. West
        1995, 1997, 1994, 1995, 1992, 
        1995, 1996, 1994, 1994, 1996,

        # Rise of Southern Rap
        1991, 1996, 1994, 1999, 2000, 
        1999, 2006, 2003, 2000, 2004,

        # Bling Era
        2003, 2002, 2004, 2000, 2003, 
        2004, 2005, 2005, 2001, 1998,

        # Conscious Resurgence
        2015, 2004, 2005, 2017, 2012, 
        2017, 2015, 2016, 2010, 2010,

        # Blog Era & Trap
        2018, 2017, 2017, 2017, 2017, 
        2018, 2015, 2018, 2018, 2019
    ],
    "Era": [
        # Old School
        "Old School", "Old School", "Old School", "Old School", "Old School", 
        "Old School", "Old School", "Old School", "Old School", "Old School",
        
        # Golden Age
        "Golden Age", "Golden Age", "Golden Age", "Golden Age", "Golden Age", 
        "Golden Age", "Golden Age", "Golden Age", "Golden Age", "Golden Age",
        
        # East vs. West
        "East vs. West", "East vs. West", "East vs. West", "East vs. West", "East vs. West",
        "East vs. West", "East vs. West", "East vs. West", "East vs. West", "East vs. West",

        # Rise of Southern Rap
        "Southern Rap", "Southern Rap", "Southern Rap", "Southern Rap", "Southern Rap", 
        "Southern Rap", "Southern Rap", "Southern Rap", "Southern Rap", "Southern Rap",

        # Bling Era
        "Bling Era", "Bling Era", "Bling Era", "Bling Era", "Bling Era", 
        "Bling Era", "Bling Era", "Bling Era", "Bling Era", "Bling Era",

        # Conscious Resurgence
        "Conscious Resurgence", "Conscious Resurgence", "Conscious Resurgence", "Conscious Resurgence", "Conscious Resurgence",
        "Conscious Resurgence", "Conscious Resurgence", "Conscious Resurgence", "Conscious Resurgence", "Conscious Resurgence",

        # Blog Era & Trap
        "Blog Era & Trap", "Blog Era & Trap", "Blog Era & Trap", "Blog Era & Trap", "Blog Era & Trap",
        "Blog Era & Trap", "Blog Era & Trap", "Blog Era & Trap", "Blog Era & Trap", "Blog Era & Trap"
    ]
}

# Creating the dataframe
df = pd.DataFrame(data)

# Saving it to a CSV file
#file_path = "/mnt/data/hiphop_eras_songs.csv"
df.to_csv()

# Display the file path so the user can download

