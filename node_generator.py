import redis
import os
import sys
import random
import time
from dotenv import load_dotenv

load_dotenv()

redisClient = redis.from_url(os.getenv('REDIS_URL'), decode_responses=True)

first_names = [
"John", "William", "James", "Charles", "George", "Frank", "Joseph", "Thomas", "Henry", "Robert", "Edward", "Harry", "Walter", "Arthur", "Fred", "Albert", "Samuel", "David", "Louis", "Joe", "Charlie", "Clarence", "Richard", "Andrew", "Daniel", "Ernest", "Will", "Jesse", "Oscar", "Lewis", "Peter", "Benjamin", "Frederick", "Willie", "Alfred", "Sam", "Roy", "Herbert", "Jacob", "Tom", "Elmer", "Carl", "Lee", "Howard", "Martin", "Michael", "Bert", "Herman", "Jim", "Francis", "Harvey", "Earl", "Eugene", "Ralph", "Ed", "Claude", "Edwin", "Ben", "Charley", "Paul", "Edgar", "Isaac", "Otto", "Luther", "Lawrence", "Ira", "Patrick", "Guy", "Oliver", "Theodore", "Hugh", "Clyde", "Alexander", "August", "Floyd", "Homer", "Jack", "Leonard", "Horace", "Marion", "Philip", "Allen", "Archie", "Stephen", "Chester", "Willis", "Raymond", "Rufus", "Warren", "Jessie", "Milton", "Alex", "Leo", "Julius", "Ray", "Sidney", "Bernard", "Dan", "Jerry", "Calvin", "Perry", "Dave", "Anthony", "Eddie", "Amos", "Dennis", "Clifford", "Leroy", "Wesley", "Alonzo", "Garfield", "Franklin", "Emil", "Leon", "Nathan", "Harold", "Matthew", "Levi", "Moses", "Everett", "Lester", "Winfield", "Adam", "Lloyd", "Mack", "Fredrick", "Jay", "Jess", "Melvin", "Noah", "Aaron", "Alvin", "Norman", "Gilbert", "Elijah", "Victor", "Gus", "Nelson", "Jasper", "Silas", "Christopher", "Jake", "Mike", "Percy", "Adolph", "Maurice", "Cornelius", "Felix", "Reuben", "Wallace", "Claud", "Roscoe", "Sylvester", "Earnest", "Hiram", "Otis", "Simon", "Willard", "Irvin", "Mark", "Jose", "Wilbur", "Abraham", "Virgil", "Clinton", "Elbert", "Leslie", "Marshall", "Owen", "Wiley", "Anton", "Morris", "Manuel", "Phillip", "Augustus", "Emmett", "Eli", "Nicholas", "Wilson", "Alva", "Harley", "Newton", "Timothy", "Marvin", "Ross", "Curtis", "Edmund", "Jeff", "Elias", "Harrison", "Stanley", "Columbus", "Lon", "Ora", "Ollie", "Russell", "Pearl", "Solomon", "Arch", "Asa", "Clayton", "Enoch", "Irving", "Mathew", "Nathaniel", "Scott", "Hubert", "Lemuel", "Andy", "Ellis", "Emanuel", "Joshua", "Millard", "Vernon", "Wade", "Cyrus", "Miles", "Rudolph", "Sherman", "Austin", "Bill", "Chas", "Lonnie", "Monroe", "Byron", "Edd", "Emery", "Grant", "Jerome", "Max", "Mose", "Steve", "Gordon", "Abe", "Pete", "Chris", "Clark", "Gustave", "Orville", "Lorenzo", "Bruce", "Marcus", "Preston", "Bob", "Dock", "Donald", "Jackson", "Cecil", "Barney", "Delbert", "Edmond", "Anderson", "Christian", "Glenn", "Jefferson", "Luke", "Neal", "Burt", "Ike", "Myron", "Tony", "Conrad", "Joel", "Matt", "Riley", "Vincent", "Emory", "Isaiah", "Nick", "Ezra", "Green", "Juan", "Clifton", "Lucius", "Porter", "Arnold", "Bud", "Jeremiah", "Taylor", "Forrest", "Roland", "Spencer", "Burton", "Don", "Emmet", "Gustav", "Louie", "Morgan", "Ned", "Van", "Ambrose", "Chauncey", "Elisha", "Ferdinand", "General", "Julian", "Kenneth", "Mitchell", "Allie", "Josh", "Judson", "Lyman", "Napoleon", "Pedro", "Berry", "Dewitt", "Ervin", "Forest", "Lynn", "Pink", "Ruben", "Sanford", "Ward", "Douglas", "Ole", "Omer", "Ulysses", "Walker", "Wilbert", "Adelbert", "Benjiman", "Ivan", "Jonas", "Major", "Abner", "Archibald", "Caleb", "Clint", "Dudley", "Granville", "King", "Mary", "Merton", "Antonio", "Bennie", "Carroll", "Freeman", "Josiah", "Milo", "Royal", "Dick", "Earle", "Elza", "Emerson", "Fletcher", "Judge", "Laurence", "Neil", "Roger", "Seth", "Glen", "Hugo", "Jimmie", "Johnnie", "Washington", "Elwood", "Gust", "Harmon", "Jordan", "Simeon", "Wayne", "Wilber", "Clem", "Evan", "Frederic", "Irwin", "Junius", "Lafayette", "Loren", "Madison", "Mason", "Orval", "Abram", "Aubrey", "Elliott", "Hans", "Karl", "Minor", "Wash", "Wilfred", "Allan", "Alphonse", "Dallas", "Dee", "Isiah", "Jason", "Johnny", "Lawson", "Lew", "Micheal", "Orin", "Addison", "Cal", "Erastus", "Francisco", "Hardy", "Lucien", "Randolph", "Stewart", "Vern", "Wilmer", "Zack", "Adrian", "Alvah", "Bertram", "Clay", "Ephraim", "Fritz", "Giles", "Grover", "Harris", "Isom", "Jesus", "Johnie", "Jonathan", "Lucian", "Malcolm", "Merritt", "Otho", "Perley", "Rolla", "Sandy", "Tomas", "Wilford", "Adolphus", "Angus", "Arther", "Carlos", "Cary", "Cassius", "Davis", "Hamilton", "Harve", "Israel", "Leander", "Melville", "Merle", "Murray", "Pleasant", "Sterling", "Steven", "Axel", "Boyd", "Bryant", "Clement", "Erwin", "Ezekiel", "Foster", "Frances", "Geo", "Houston", "Issac", "Jules", "Larkin", "Mat", "Morton", "Orlando", "Pierce", "Prince", "Rollie", "Rollin", "Sim", "Stuart", "Wilburn", "Bennett", "Casper", "Christ", "Dell", "Egbert", "Elmo", "Fay", "Gabriel", "Hector", "Horatio", "Lige", "Saul", "Smith", "Squire", "Tobe", "Tommie", "Wyatt", "Alford", "Alma", "Alton", "Andres", "Burl", "Cicero", "Dean", "Dorsey", "Enos", "Howell", "Lou", "Loyd", "Mahlon", "Nat", "Omar", "Oran", "Parker", "Raleigh", "Reginald", "Rubin", "Seymour", "Wm", "Young", "Benjamine", "Carey", "Carlton", "Eldridge", "Elzie", "Garrett", "Isham", "Johnson", "Larry", "Logan", "Merrill", "Mont", "Oren", "Pierre", "Rex", "Rodney", "Ted", "Webster", "West", "Wheeler", "Willam", "Al", "Aloysius", "Alvie", "Anna", "Art", "Augustine", "Bailey", "Benjaman", "Beverly", "Bishop", "Clair", "Cloyd", "Coleman", "Dana", "Duncan", "Dwight", "Emile", "Evert", "Henderson", "Hunter", "Jean", "Lem", "Luis", "Mathias", "Maynard", "Miguel", "Mortimer", "Nels", "Norris", "Pat", "Phil", "Rush", "Santiago", "Sol", "Sydney", "Thaddeus", "Thornton", "Tim", "Travis", "Truman", "Watson", "Webb", "Wellington", "Winfred", "Wylie", "Alec", "Basil", "Baxter", "Bertrand", "Buford", "Burr", "Cleveland", "Colonel", "Dempsey", "Early", "Ellsworth", "Fate", "Finley", "Gabe", "Garland", "Gerald", "Herschel", "Hezekiah", "Justus", "Lindsey", "Marcellus", "Olaf", "Olin", "Pablo", "Rolland", "Turner", "Verne", "Volney", "Williams", "Almon", "Alois", "Alonza", "Anson", "Authur", "Benton", "Billie", "Cornelious", "Darius", "Denis", "Dillard", "Doctor", "Elvin", "Emma", "Eric", "Evans", "Gideon", "Haywood", "Hilliard", "Hosea", "Lincoln", "Lonzo", "Lucious", "Lum", "Malachi", "Newt", "Noel", "Orie", "Palmer", "Pinkney", "Shirley", "Sumner", "Terry", "Urban", "Uriah", "Valentine", "Waldo", "Warner", "Wong", "Zeb", "Abel", "Alden", "Archer", "Avery", "Carson", "Cullen", "Doc", "Eben", "Elige", "Elizabeth", "Elmore", "Ernst", "Finis", "Freddie", "Godfrey", "Guss", "Hamp", "Hermann", "Isadore", "Isreal", "Jones", "June", "Lacy", "Lafe", "Leland", "Llewellyn", "Ludwig", "Manford", "Maxwell", "Minnie", "Obie", "Octave", "Orrin", "Ossie", "Oswald", "Park", "Parley", "Ramon", "Rice", "Stonewall", "Theo", "Tillman", "Addie", "Aron", "Ashley", "Bernhard", "Bertie", "Berton", "Buster", "Butler", "Carleton", "Carrie", "Clara", "Clarance", "Clare", "Crawford", "Danial", "Dayton", "Dolphus", "Elder", "Ephriam", "Fayette", "Felipe", "Fernando", "Flem", "Florence", "Ford", "Harlan", "Hayes", "Henery", "Hoy", "Huston", "Ida", "Ivory", "Jonah", "Justin", "Lenard", "Leopold", "Lionel", "Manley", "Marquis", "Marshal", "Mart", "Odie", "Olen", "Oral", "Orley", "Otha", "Press", "Price", "Quincy", "Randall", "Rich", "Richmond", "Romeo", "Russel", "Rutherford", "Shade", "Shelby", "Solon", "Thurman", "Tilden", "Troy", "Woodson", "Worth", "Aden", "Alcide", "Alf", "Algie", "Arlie", "Bart", "Bedford", "Benito", "Billy", "Bird", "Birt", "Bruno", "Burley", "Chancy", "Claus", "Cliff", "Clovis", "Connie", "Creed", "Delos", "Duke", "Eber", "Eligah", "Elliot", "Elton", "Emmitt", "Gene", "Golden", "Hal", "Hardin", "Harman", "Hervey", "Hollis", "Ivey", "Jennie", "Len", "Lindsay", "Lonie", "Lyle", "Mac", "Mal", "Math", "Miller", "Orson", "Osborne", "Percival", "Pleas", "Ples", "Rafael", "Raoul", "Roderick", "Rose", "Shelton", "Sid", "Theron", "Tobias", "Toney", "Tyler", "Vance", "Vivian", "Walton", "Watt", "Weaver", "Wilton", "Adolf", "Albin", "Albion", "Allison", "Alpha", "Alpheus", "Anastacio", "Andre", "Annie", "Arlington", "Armand", "Asberry", "Asbury", "Asher", "Augustin", "Auther", "Author", "Ballard", "Blas", "Caesar", "Candido", "Cato", "Clarke", "Clemente", "Colin", "Commodore", "Cora", "Coy", "Cruz", "Curt", "Damon", "Davie", "Delmar", "Dexter", "Dora", "Doss", "Drew", "Edson", "Elam", "Elihu", "Eliza", "Elsie", "Erie", "Ernie", "Ethel", "Ferd", "Friend", "Garry", "Gary", "Grace", "Gustaf", "Hallie", "Hampton", "Harrie", "Hattie", "Hence", "Hillard", "Hollie", "Holmes", "Hope", "Hyman", "Ishmael", "Jarrett", "Jessee", "Joeseph", "Junious", "Kirk", "Levy", "Mervin", "Michel", "Milford", "Mitchel", "Nellie", "Noble", "Obed", "Oda", "Orren", "Ottis", "Rafe", "Redden", "Reese", "Rube", "Ruby", "Rupert", "Salomon", "Sammie", "Sanders", "Soloman", "Stacy", "Stanford", "Stanton", "Thad", "Titus", "Tracy", "Vernie", "Wendell", "Wilhelm", "Willian", "Yee", "Zeke", "Ab", "Abbott", "Agustus", "Albertus", "Almer", "Alphonso", "Alvia", "Artie", "Arvid", "Ashby", "Augusta", "Aurthur", "Babe", "Baldwin", "Barnett", "Bartholomew", "Barton", "Bernie", "Blaine", "Boston", "Brad", "Bradford", "Bradley", "Brooks", "Buck", "Budd", "Ceylon", "Chalmers", "Chesley", "Chin", "Cleo", "Crockett", "Cyril", "Daisy", "Denver", "Dow", "Duff", "Edie", "Edith", "Elick", "Elie", "Eliga", "Eliseo", "Elroy", "Ely", "Ennis", "Enrique", "Erasmus", "Esau", "Everette", "Firman", "Fleming", "Flora", "Gardner", "Gee", "Gorge", "Gottlieb", "Gregorio", "Gregory", "Gustavus", "Halsey", "Handy", "Hardie", "Harl", "Hayden", "Hays", "Hermon", "Hershel", "Holly", "Hosteen", "Hoyt", "Hudson", "Huey", "Humphrey", "Hunt", "Hyrum", "Irven", "Isam", "Ivy", "Jabez", "Jewel", "Jodie", "Judd", "Julious", "Justice", "Katherine", "Kelly", "Kit", "Knute", "Lavern", "Lawyer", "Layton"
]

last_names = [
"Emma", "Isabella", "Emily", "Madison", "Ava", "Olivia", "Sophia", "Abigail", "Elizabeth", "Chloe", "Samantha", "Addison", "Natalie", "Mia", "Alexis", "Alyssa", "Hannah", "Ashley", "Ella", "Sarah", "Grace", "Taylor", "Brianna", "Lily", "Hailey", "Anna", "Victoria", "Kayla", "Lillian", "Lauren", "Kaylee", "Allison", "Savannah", "Nevaeh", "Gabriella", "Sofia", "Makayla", "Avery", "Riley", "Julia", "Leah", "Aubrey", "Jasmine", "Audrey", "Katherine", "Morgan", "Brooklyn", "Destiny", "Sydney", "Alexa", "Kylie", "Brooke", "Kaitlyn", "Evelyn", "Layla", "Madeline", "Kimberly", "Zoe", "Jessica", "Peyton", "Alexandra", "Claire", "Madelyn", "Maria", "Mackenzie", "Arianna", "Jocelyn", "Amelia", "Angelina", "Trinity", "Andrea", "Maya", "Valeria", "Sophie", "Rachel", "Vanessa", "Aaliyah", "Mariah", "Gabrielle", "Katelyn", "Ariana", "Bailey", "Camila", "Jennifer", "Melanie", "Gianna", "Charlotte", "Paige", "Autumn", "Payton", "Faith", "Sara", "Isabelle", "Caroline", "Genesis", "Isabel", "Mary", "Zoey", "Gracie", "Megan", "Haley", "Mya", "Michelle", "Molly", "Stephanie", "Nicole", "Jenna", "Natalia", "Sadie", "Jada", "Serenity", "Lucy", "Ruby", "Eva", "Kennedy", "Rylee", "Jayla", "Naomi", "Rebecca", "Lydia", "Daniela", "Bella", "Keira", "Adriana", "Lilly", "Hayden", "Miley", "Katie", "Jade", "Jordan", "Gabriela", "Amy", "Angela", "Melissa", "Valerie", "Giselle", "Diana", "Amanda", "Kate", "Laila", "Reagan", "Jordyn", "Kylee", "Danielle", "Briana", "Marley", "Leslie", "Kendall", "Catherine", "Liliana", "Mckenzie", "Jacqueline", "Ashlyn", "Reese", "Marissa", "London", "Juliana", "Shelby", "Cheyenne", "Angel", "Daisy", "Makenzie", "Miranda", "Erin", "Amber", "Alana", "Ellie", "Breanna", "Ana", "Mikayla", "Summer", "Piper", "Adrianna", "Jillian", "Sierra", "Jayden", "Sienna", "Alicia", "Lila", "Margaret", "Alivia", "Brooklynn", "Karen", "Violet", "Sabrina", "Stella", "Aniyah", "Annabelle", "Alexandria", "Kathryn", "Skylar", "Aliyah", "Delilah", "Julianna", "Kelsey", "Khloe", "Carly", "Amaya", "Mariana", "Christina", "Alondra", "Tessa", "Eliana", "Bianca", "Jazmin", "Clara", "Vivian", "Josephine", "Delaney", "Scarlett", "Elena", "Cadence", "Alexia", "Maggie", "Laura", "Nora", "Ariel", "Elise", "Nadia", "Mckenna", "Chelsea", "Lyla", "Alaina", "Jasmin", "Hope", "Leila", "Caitlyn", "Cassidy", "Makenna", "Allie", "Izabella", "Eden", "Callie", "Haylee", "Caitlin", "Kendra", "Karina", "Kyra", "Kayleigh", "Addyson", "Kiara", "Jazmine", "Karla", "Camryn", "Alina", "Lola", "Kyla", "Kelly", "Fatima", "Tiffany", "Kira", "Crystal", "Mallory", "Esmeralda", "Alejandra", "Eleanor", "Angelica", "Jayda", "Abby", "Kara", "Veronica", "Carmen", "Jamie", "Ryleigh", "Valentina", "Allyson", "Dakota", "Kamryn", "Courtney", "Cecilia", "Madeleine", "Aniya", "Alison", "Esther", "Heaven", "Aubree", "Lindsey", "Leilani", "Nina", "Melody", "Macy", "Ashlynn", "Joanna", "Cassandra", "Alayna", "Kaydence", "Madilyn", "Aurora", "Heidi", "Emerson", "Kimora", "Madalyn", "Erica", "Josie", "Katelynn", "Guadalupe", "Harper", "Ivy", "Lexi", "Camille", "Savanna", "Dulce", "Daniella", "Lucia", "Emely", "Joselyn", "Kiley", "Kailey", "Miriam", "Cynthia", "Rihanna", "Georgia", "Rylie", "Harmony", "Kiera", "Kyleigh", "Monica", "Bethany", "Kaylie", "Cameron", "Teagan", "Cora", "Brynn", "Ciara", "Genevieve", "Alice", "Maddison", "Eliza", "Tatiana", "Jaelyn", "Erika", "Ximena", "April", "Marely", "Julie", "Danica", "Presley", "Brielle", "Julissa", "Angie", "Iris", "Brenda", "Hazel", "Rose", "Malia", "Shayla", "Fiona", "Phoebe", "Nayeli", "Paola", "Kaelyn", "Selena", "Audrina", "Rebekah", "Carolina", "Janiyah", "Michaela", "Penelope", "Janiya", "Anastasia", "Adeline", "Ruth", "Sasha", "Denise", "Holly", "Madisyn", "Hanna", "Tatum", "Marlee", "Nataly", "Helen", "Janelle", "Lizbeth", "Serena", "Anya", "Jaslene", "Kaylin", "Jazlyn", "Nancy", "Lindsay", "Desiree", "Hayley", "Itzel", "Imani", "Madelynn", "Asia", "Kadence", "Madyson", "Talia", "Jane", "Kayden", "Annie", "Amari", "Bridget", "Raegan", "Jadyn", "Celeste", "Jimena", "Luna", "Yasmin", "Emilia", "Annika", "Estrella", "Sarai", "Lacey", "Ayla", "Alessandra", "Willow", "Nyla", "Dayana", "Lilah", "Lilliana", "Natasha", "Hadley", "Harley", "Priscilla", "Claudia", "Allisson", "Baylee", "Brenna", "Brittany", "Skyler", "Fernanda", "Danna", "Melany", "Cali", "Lia", "Macie", "Lyric", "Logan", "Gloria", "Lana", "Mylee", "Cindy", "Lilian", "Amira", "Anahi", "Alissa", "Anaya", "Lena", "Ainsley", "Sandra", "Noelle", "Marisol", "Meredith", "Kailyn", "Lesly", "Johanna", "Diamond", "Evangeline", "Juliet", "Kathleen", "Meghan", "Paisley", "Athena", "Hailee", "Rosa", "Wendy", "Emilee", "Sage", "Alanna", "Elaina", "Cara", "Nia", "Paris", "Casey", "Dana", "Emery", "Rowan", "Aubrie", "Kaitlin", "Jaden", "Kenzie", "Kiana", "Viviana", "Norah", "Lauryn", "Perla", "Amiyah", "Alyson", "Rachael", "Shannon", "Aileen", "Miracle", "Lillie", "Danika", "Heather", "Kassidy", "Taryn", "Tori", "Francesca", "Kristen", "Amya", "Elle", "Kristina", "Cheyanne", "Haylie", "Patricia", "Anne", "Samara", "Skye", "Kali", "America", "Lexie", "Parker", "Halle", "Londyn", "Abbigail", "Linda", "Hallie", "Saniya", "Bryanna", "Bailee", "Jaylynn", "Mckayla", "Quinn", "Jaelynn", "Jaida", "Caylee", "Jaiden", "Melina", "Abril", "Sidney", "Kassandra", "Elisabeth", "Adalyn", "Kaylynn", "Mercedes", "Yesenia", "Elliana", "Brylee", "Dylan", "Isabela", "Ryan", "Ashlee", "Daphne", "Kenya", "Marina", "Christine", "Mikaela", "Kaitlynn", "Justice", "Saniyah", "Jaliyah", "Ingrid", "Marie", "Natalee", "Joy", "Juliette", "Simone", "Adelaide", "Krystal", "Kennedi", "Mila", "Tamia", "Addisyn", "Aylin", "Dayanara", "Sylvia", "Clarissa", "Maritza", "Virginia", "Braelyn", "Jolie", "Jaidyn", "Kinsley", "Kirsten", "Laney", "Marilyn", "Whitney", "Janessa", "Raquel", "Anika", "Kamila", "Aria", "Rubi", "Adelyn", "Amara", "Ayanna", "Teresa", "Zariah", "Kaleigh", "Amani", "Carla", "Yareli", "Gwendolyn", "Paulina", "Nathalie", "Annabella", "Jaylin", "Tabitha", "Deanna", "Madalynn", "Journey", "Aiyana", "Skyla", "Yaretzi", "Ada", "Liana", "Karlee", "Jenny", "Myla", "Cristina", "Myah", "Lisa", "Tania", "Isis", "Jayleen", "Jordin", "Arely", "Azul", "Helena", "Aryanna", "Jaqueline", "Lucille", "Destinee", "Martha", "Zoie", "Arielle", "Liberty", "Marlene", "Elisa", "Isla", "Noemi", "Raven", "Jessie", "Aleah", "Kailee", "Kaliyah", "Lilyana", "Haven", "Tara", "Giana", "Camilla", "Maliyah", "Irene", "Carley", "Maeve", "Lea", "Macey", "Sharon", "Alisha", "Marisa", "Jaylene", "Kaya", "Scarlet", "Siena", "Adyson", "Maia", "Shiloh", "Tiana", "Jaycee", "Gisselle", "Yazmin", "Eve", "Shyanne", "Arabella", "Sherlyn", "Sariah", "Amiya", "Kiersten", "Madilynn", "Shania", "Aleena", "Finley", "Kinley", "Kaia", "Aliya", "Taliyah", "Pamela", "Yoselin", "Ellen", "Carlie", "Monserrat", "Jakayla", "Reyna", "Yaritza", "Carolyn", "Clare", "Lorelei", "Paula", "Zaria", "Gracelyn", "Kasey", "Regan", "Alena", "Angelique", "Regina", "Britney", "Emilie", "Mariam", "Jaylee", "Julianne", "Greta", "Elyse", "Lainey", "Kallie", "Felicity", "Zion", "Aspen", "Carlee", "Annalise", "Iliana", "Larissa", "Akira", "Sonia", "Catalina", "Phoenix", "Joslyn", "Anabelle", "Mollie", "Susan", "Judith", "Destiney", "Hillary", "Janet", "Katrina", "Mareli", "Ansley", "Kaylyn", "Alexus", "Gia", "Maci", "Elsa", "Stacy", "Kaylen", "Carissa", "Haleigh", "Lorena", "Jazlynn", "Milagros", "Luz", "Leanna", "Renee", "Shaniya", "Charlie", "Abbie", "Cailyn", "Cherish", "Elsie", "Jazmyn", "Elaine", "Emmalee", "Luciana", "Dahlia", "Jamya", "Belinda", "Mariyah", "Chaya", "Dayami", "Rhianna", "Yadira", "Aryana", "Rosemary", "Armani", "Cecelia", "Celia", "Barbara", "Cristal", "Eileen", "Rayna", "Campbell", "Amina", "Aisha", "Amirah", "Ally", "Araceli", "Averie", "Mayra", "Sanaa", "Patience", "Leyla", "Selah", "Zara", "Chanel", "Kaiya", "Keyla", "Miah", "Aimee", "Giovanna", "Amelie", "Kelsie", "Alisson", "Angeline", "Dominique", "Adrienne", "Brisa", "Cierra", "Paloma", "Isabell", "Precious", "Alma", "Charity", "Jacquelyn", "Janae", "Frances", "Shyla", "Janiah", "Kierra", "Karlie", "Annabel", "Jacey", "Karissa", "Jaylah", "Xiomara", "Edith", "Marianna", "Damaris", "Deborah", "Jaylyn", "Evelin", "Mara", "Olive", "Ayana", "India", "Kendal", "Kayley", "Tamara", "Briley", "Charlee", "Nylah", "Abbey", "Moriah", "Saige", "Savanah", "Giada", "Hana", "Lizeth", "Matilda", "Ann", "Jazlene", "Gillian", "Beatrice", "Ireland", "Karly", "Mylie", "Yasmine", "Ashly", "Kenna", "Maleah", "Corinne", "Keely", "Tanya", "Tianna", "Adalynn", "Ryann", "Salma", "Areli", "Karma", "Shyann", "Kaley", "Theresa", "Evie", "Gina", "Roselyn", "Kaila", "Jaylen", "Natalya", "Meadow", "Rayne", "Aliza", "Yuliana", "June", "Lilianna", "Nathaly", "Ali", "Alisa", "Aracely", "Belen", "Tess", "Jocelynn", "Litzy", "Makena", "Abagail", "Giuliana", "Joyce", "Libby", "Lillianna", "Thalia", "Tia", "Sarahi", "Zaniyah", "Kristin", "Lorelai", "Mattie", "Taniya", "Jaslyn", "Gemma", "Valery", "Lailah", "Mckinley", "Micah", "Deja", "Frida", "Brynlee", "Jewel", "Krista", "Mira", "Yamilet", "Adison", "Carina", "Karli", "Magdalena", "Stephany", "Charlize", "Raelynn", "Aliana", "Cassie", "Mina", "Karley", "Shirley", "Marlie", "Alani", "Taniyah", "Cloe", "Sanai", "Lina", "Nola", "Anabella", "Dalia", "Raina", "Mariela", "Ariella", "Bria", "Kamari", "Monique", "Ashleigh", "Reina", "Alia", "Ashanti", "Lara", "Lilia", "Justine", "Leia", "Maribel", "Abigayle", "Tiara", "Alannah", "Princess", "Sydnee", "Kamora", "Paityn", "Payten", "Naima", "Gretchen", "Heidy", "Nyasia", "Livia", "Marin", "Shaylee", "Maryjane", "Laci", "Nathalia", "Azaria", "Anabel", "Chasity", "Emmy", "Izabelle", "Denisse", "Emelia", "Mireya", "Shea", "Amiah", "Dixie", "Maren", "Averi", "Esperanza", "Micaela", "Selina", "Alyvia", "Chana", "Avah", "Donna", "Kaylah", "Ashtyn", "Karsyn", "Makaila", "Shayna", "Essence", "Leticia", "Miya", "Rory", "Desirae", "Kianna", "Laurel", "Neveah", "Amaris", "Hadassah", "Dania", "Hailie", "Jamiya", "Kathy", "Laylah", "Riya", "Diya", "Carleigh", "Iyana", "Kenley", "Sloane", "Elianna"
]

cities = [
"Cape Town", "New York", "London", "Paris", "Tokyo", "Shanghai", "Mexico City", "Mumbai", "Beijing", "Istanbul", "Kolkata", "Buenos Aires", "Osaka", "Shenzhen", "Lahore", "Bangalore", "Seoul", "Bangkok", "Baghdad", "Hong Kong", "Miami", "Atlanta", "Dar es Salaam", "Guadalajara"
]

def generate_first_name():
    return random.choice(first_names)


def generate_last_name():
    return random.choice(last_names)


def generate_age():
    return random.randint(0, 100)


def generate_sex():
    return random.choice(['M', 'F'])


def generate_city():
    return random.choice(cities)


def generate_string():
    return "x" * random.randint(0, 50)


def generate_relationships(total):
    rels = []

    for i in range(10):
        rels.append(f'n:{random.randint(0, total)}')

    return rels


def run(nodes=1000000, properties=20, relationships=10):
    """
    Generate mock nodes with properties and flattened relationships
    """
    print(f'Starting node generator nodes={nodes}, properties={properties}, relationships={relationships}')

    pipe = redisClient.pipeline(transaction=False)
    for i in range(nodes):
        pipe.hset(f'n:{i}', mapping={
            'first_name': generate_first_name(),
            'last_name': generate_last_name(),
            'sex': generate_sex(),
            'age': generate_age(),
            'city': generate_city(),
            'property6': generate_string(),
            'property7': generate_string(),
            'property8': generate_string(),
            'property9': generate_string(),
            'property10': generate_string(),
            'property11': generate_string(),
            'property12': generate_string(),
            'property13': generate_string(),
            'property14': generate_string(),
            'property15': generate_string(),
            'property16': generate_string(),
            'property17': generate_string(),
            'property18': generate_string(),
            'property19': generate_string(),
            'property20': generate_string(),
            'rels': ",".join(generate_relationships(nodes))
        })
        if i % 1000 == 0:
            pipe.execute()
            pipe = redisClient.pipeline(transaction=False)

    pipe.execute()

if __name__ == "__main__":
    """
    Example: python cdr_generator.py events:cdr
    """
    run()
