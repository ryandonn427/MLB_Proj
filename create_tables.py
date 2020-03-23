from connect import Connect
from datetime import datetime
a = Connect()
a.connect()
"""
CREATE TABLE gameData_players (
    nameMatrilineal text,
    strikeZoneBottom decimal,
    lastFirstName      	text,
    birthCountry       	text,
    primaryPositionname	text,
    fullFMLName        	text,
    birthCity	text,
    primaryNumber      	smallint,
    nickName	text,
    batSidedescription 	text,
    height	text,
    lastInitName       	text,
    fullLFMName        	text,
    gender	char(1),
    strikeZoneTop	decimal,
    isPlayer	boolean,
    mlbDebutDate	date,
    pronunciation	text,
    pitchHandcode	char(1),
    deathCity	text,
    deathStateProvince	text,
    nameSlug	text,
    firstLastName	text,
    initLastName	text,
    draftYear	integer,
    nameTitle	text,
    deathCountry	text,
    useName	text,
    nameFirstLast	text,
    birthDate	date,
    weight	smallint,
    deathDate	date,
    currentAge	smallint,
    primaryPositiontype	text,
    link	text,
    isVerified	boolean,
    firstName	text,
    middleName	text,
    birthStateProvince	text,
    lastName	text,
    lastPlayedDate	date,
    gameid	integer,
    boxscoreName	text,
    primaryPositionabbreviation	varchar(3),
    fullName	text,
    active	boolean,
    batSidecode	char(1),
    primaryPositioncode	smallint,
    id	integer,
    pitchHanddescription	text
)
"""
"""
CREATE TABLE gameData_probablePitchers (
    gameid	integer,
    ha	text,
    fullName	text,
    id	integer,
    link	text

)
"""
"""
CREATE TABLE gameData_teams (
    teamName	text,
    leagueid	smallint,
    sportlink	text,
    leaguename	text,
    name	text,
    recordwildCardGamesBack	integer,
    divisionname	text,
    venueid	smallint,
    season	integer,
    locationName	text,
    divisionlink	text,
    recordgamesPlayed	integer,
    fileCode	varchar(3),
    venuelink	text,
    springLeaguename	text,
    leaguelink	text,
    springLeagueabbreviation	varchar(3),
    recordspringLeagueGamesBack	integer,
    venuename	text,
    recorddivisionGamesBack	integer,
    springLeagueid	integer,
    recordsportGamesBack	integer,
    abbreviation	varchar(3),
    firstYearOfPlay	integer,
    springLeaguelink	text,
    sportname	text,
    link	text,
    teamCode	varchar(3),
    shortName	text,
    recordconferenceGamesBack	integer,
    gameid	integer,
    recordleagueRecordwins	integer,
    divisionid	integer,
    sportid	integer,
    recordleagueRecordlosses	integer,
    active	boolean,
    recordleagueGamesBack	integer,
    recordleagueRecordpct	decimal,
    id	integer,
    allStarStatus	char(1)
)
"""

"""
CREATE TABLE gameData_venue (
    fieldInfoleftLine	integer,
    fieldInfoleft	integer,
    name	text,
    timeZoneid	integer,
    fieldInforight	integer,
    locationdefaultCoordinateslatitude	decimal,
    locationcity	text,
    timeZoneoffset	text,
    fieldInforightCenter	integer,
    fieldInforoofType	text,
    fieldInfoleftCenter	integer,
    fieldInfoturfType	text,
    fieldInfocenter	integer,
    link	text,
    locationcountry	text,
    fieldInforightLine	integer,
    gameid	integer,
    locationstate	text,
    locationdefaultCoordinateslongitude	decimal,
    timeZonetz	varchar(3),
    fieldInfocapacity	integer,
    locationstateAbbrev	varchar(3),
    id	integer

)
"""
"""
CREATE TABLE liveData_plays_result (
    description	text,
    gameid	integer,
    eventType	text,
    rbi	smallint,
    event	text,
    atbatid	smallint,
    type	text,
    awayScore	smallint,
    homeScore	smallint

)
"""
"""
CREATE TABLE liveData_plays_about (
    hasOut	boolean,
    isComplete	boolean,
    captivatingIndex	smallint,
    isTopInning	boolean,
    isScoringPlay	boolean,
    inning	smallint,
    gameid	integer,
    atbatid	smallint,
    endTime	timestamp,
    hasReview	boolean,
    atBatIndex	smallint,
    startTime	timestamp,
    halfInning	text

)
"""

"""
CREATE TABLE liveData_plays_count (
    gameid	integer,
    balls	smallint,
    outs	smallint,
    strikes	smallint,
    atbatid	smallint

)
"""
"""
CREATE TABLE liveData_plays_matchup (
    atbatid	smallint,
    batSidecode	char(1),
    batSidedescription	text,
    batterfullName	text,
    batterid	integer,
    batterlink	text,
    firstfullName	text,
    firstid	integer,
    firstlink	text,
    gameid	integer,
    pitcherfullName	text,
    pitcherid	integer,
    pitcherlink	text,
    pitchHandcode	char(1),
    pitchHanddescription	text,
    postOnFirstfullName	text,
    postOnFirstid	integer,
    postOnFirstlink	text,
    postOnSecondfullName	text,
    postOnSecondid	integer,
    postOnSecondlink	text,
    postOnThirdfullName	text,
    postOnThirdid	integer,
    postOnThirdlink	text,
    secondfullName	text,
    secondid	integer,
    secondlink	text,
    splitsbatter	text,
    splitsmenOnBase	text,
    splitspitcher	text,
    thirdfullName	text,
    thirdid	integer,
    thirdlink	text
)
"""
"""
CREATE TABLE liveData_plays_runners (
    atbatid	smallint,
    creditscredit	text,
    creditsplayerid	integer,
    creditsplayerlink	text,
    creditspositionabbreviation	varchar(2),
    creditspositioncode	smallint,
    creditspositionname	text,
    creditspositiontype	text,
    detailsearned	boolean,
    detailsevent	text,
    detailseventType	text,
    detailsisScoringEvent	boolean,
    detailsmovementReason	text,
    detailsplayIndex	smallint,
    detailsrbi	boolean,
    detailsresponsiblePitcher	text,
    detailsresponsiblePitcherid	integer,
    detailsresponsiblePitcherlink	text,
    detailsrunnerfullName	text,
    detailsrunnerid	integer,
    detailsrunnerlink	text,
    detailsteamUnearned	boolean,
    gameid	integer,
    movementend	text,
    movementisOut	text,
    movementoutBase	text,
    movementoutNumber	text,
    movementstart	text,
    runnerid	smallint

)
"""
"""
CREATE TABLE liveData_plays_pitch (
    startTime	timestamp,
    endTime	timestamp,
    pitchDatacoordinatesz0	decimal,
    hitDatatrajectory	decimal,
    pitchDatastartSpeed	decimal,
    pitchDatacoordinatesaZ	decimal,
    pitchDatacoordinatesaY	decimal,
    pitchDatabreaksbreakY	decimal,
    hitDatacoordinatescoordY	decimal,
    hitDatalaunchSpeed	decimal,
    pitchDatacoordinatesx0	decimal,
    pitchDatabreaksbreakLength	decimal,
    pitchDatacoordinatespfxZ	decimal,
    hitDatacoordinatescoordX	decimal,
    pitchDatacoordinatesaX	decimal,
    pitchDatacoordinatesy0	decimal,
    pitchDatacoordinatesy	decimal,
    hitDatatotalDistance	decimal,
    hitDatalaunchAngle	decimal,
    pitchDatacoordinatespfxX	decimal,
    pitchDatacoordinatesvX0	decimal,
    pitchDatacoordinatesvY0	decimal,
    pitchDatabreaksbreakAngle	decimal,
    pitchDatastrikeZoneBottom	decimal,
    pitchDatacoordinatesvZ0	decimal,
    pitchDataendSpeed	decimal,
    pitchDatacoordinatespX	decimal,
    pitchDatacoordinatesx	decimal,
    pitchDatastrikeZoneTop	decimal,
    pitchDatabreaksspinRate	decimal,
    pitchDatacoordinatespZ	decimal,
    playerid	integer,
    umpireid	integer,
    playId	integer,
    gameid	integer,
    atbatid	smallint,
    actionPlayId	smallint,
    index	smallint,
    pfxId	smallint,
    runnerid	smallint,
    pitchNumber	smallint,
    umpirelink	text,
    detailsdescription	text,
    detailsisScoringPlay	text,
    detailscalldescription	text,
    battingOrder	text,
    base	text,
    detailsevent	text,
    playerlink	text,
    detailstypedescription	text,
    positioncode	varchar(3),
    detailsisInPlay	boolean,
    pitchDatabreaksspinDirection	decimal,
    type	text,
    positiontype	text,
    isPitch	boolean,
    detailstypecode	text,
    detailscode	text,
    hitDatahardness	smallint,
    detailsfromCatcher	boolean,
    pitchDataplateTime	decimal,
    injuryType	text,
    detailsrunnerGoing	boolean,
    detailsballColor	text,
    hitDatalocation	decimal,
    countstrikes	smallint,
    countouts	smallint,
    pitchDatatypeConfidence	decimal,
    positionname	text,
    detailsawayScore	smallint,
    positionabbreviation	varchar(3),
    pitchDatazone	integer,
    countballs	smallint,
    detailshomeScore	smallint,
    detailstrailColor	text,
    detailsisBall	boolean,
    detailsisStrike	boolean,
    pitchDataextension	decimal,
    detailshasReview	boolean,
    detailscallcode	char(1),
    detailseventType	text
    

)
"""
"""
CREATE TABLE liveData_linescore (
    hits	smallint,
    gameid	integer,
    leftOnBase	smallint,
    runs	smallint,
    ha	text,
    errors	smallint

)
"""
"""
CREATE TABLE liveData_decision (
    gameid	integer,
    wl	text,
    fullName	text,
    id	integer,
    link	text
)
"""
"""
CREATE TABLE liveData_officials (
    officiallink	text,
    gameid	integer,
    officialfullName	text,
    officialid	integer,
    officialType	text

)
"""
"""
CREATE TABLE liveData_plays_hotcold_batter (
    temp	text,
    gameid	integer,
    atbatid	smallint,
    value	decimal,
    color	text,
    zone	smallint

)
"""
"""
CREATE TABLE liveData_plays_hotcold_pitcher (
    temp	text,
    gameid	integer,
    atbatid	smallint,
    value	decimal,
    color	text,
    zone	smallint

)
"""
"""
CREATE TABLE gameData_datetime (
    gameid integer,
    datetime timestamp,
    originalDate date,
    dayNight text,
    time text,
    ampm char(2)
)
"""
"""
CREATE TABLE gameData_flags (
    gameid integer,
    noHitter boolean,
    perfectGame boolean
)
"""
"""
CREATE TABLE gameData_game (
    gameid integer,
    pk integer,
    type varchar(2),
    doubleHeader char(1),
    id text,
    gamedayType char(1),
    tiebreaker char(1),
    gameNumber smallint,
    calendarEventID text,
    season integer,
    seasonDisplay integer
)
"""
"""
CREATE TABLE gameData_officialScorer (
    gameid integer,
    id integer,
    fullName text,
    link text 
    )

"""
"""
CREATE TABLE gameData_primaryDatacaster (
    gameid integer,
    id integer,
    fullName text,
    link text
    )
"""
"""
CREATE TABLE gameData_status (
    gameid integer,
    abstractGameState text,
    codedGameState char(1),
    detailedState text,
    statusCode char(1),
    abstractGameCode char(1)
    )
"""
query = """
CREATE TABLE gameData_weather (
    gameid integer,
    condition text,
    temp smallint,
    wind text
    )
"""
"""
ALTER TABLE liveData_plays_pitch ALTER COLUMN hitDatatrajectory TYPE text
"""
"""
ALTER TABLE liveData_plays_pitch ALTER COLUMN hitDatahardness TYPE text
"""
"""
ALTER TABLE liveData_plays_pitch ALTER COLUMN playId TYPE text
"""
"""
ALTER TABLE liveData_plays_pitch ALTER COLUMN detailscallcode TYPE VARCHAR(3)
"""
"""
ALTER TABLE liveData_plays_pitch ALTER COLUMN actionplayid TYPE text

"""
"""
ALTER TABLE gameData_teams ALTER COLUMN fileCode TYPE text
"""
"""
ALTER TABLE liveData_plays_pitch ALTER COLUMN pfxId TYPE text
"""

tables = [
    'gameData_weather',
'gameData_status',
'gameData_primaryDatacaster',
'gameData_officialScorer',
'gameData_game',
'gameData_flags',
'gameData_datetime',
'liveData_plays_hotcold_pitcher',
'liveData_plays_hotcold_batter',
'liveData_officials',
'liveData_decision',
'liveData_linescore',
'liveData_plays_pitch',
'liveData_plays_runners',
'liveData_plays_matchup',
'liveData_plays_count',
'liveData_plays_about',
'liveData_plays_result',
'gameData_venue',
'gameData_teams',
'gameData_probablePitchers',
'gameData_players',
]
pk = [
('gameid',),
('gameid',),
('gameid',),
('gameid',),
('gameid',),
('gameid',),
('gameid',),
('gameid','atbatid',),
('gameid','atbatid',),
('gameid',),
('gameid',),
('gameid',),
('gameid','atbatid','runnerid',),
('gameid','atbatid','runnerid',),
('gameid','atbatid',),
('gameid','atbatid',),
('gameid','atbatid',),
('gameid','atbatid',),
('gameid',),
('gameid','id',),
('gameid','id',),
('gameid','id',),
]
"""
for i,j in zip(tables,pk):
    a.insert("ALTER TABLE {} ADD PRIMARY KEY ({});".format(i,','.join(j)))
"""
"""
a.insert("ALTER TABLE gamedata_teams ADD COLUMN parentorgname text")
"""
"""

"""
with open('table_sizes.txt','w') as file:
    for i in tables:
        #a.truncate(i)
        a.insert("SELECT gameid,COUNT(gameid) FROM {} GROUP BY gameid".format(i))
        for j in a.cur.fetchall():
            file.write("{} has {} rows for gameid {}".format(str(i),str(j[1]),str(j[0])))
            file.write('\n')


a.insert("SELECT datetime,gameid FROM gameData_datetime ORDER BY datetime")
for i in a.cur.fetchall():
    if '2017' in str(i):print(i)
"""
a.insert("AlTER TABLE livedata_linescore DROP CONSTRAINT livedata_linescore_pkey;")
a.insert("ALTER TABLE livedata_linescore ADD PRIMARY KEY (gameid,ha)")
"""
"""
a.insert("ALTER TABLE liveData_plays_pitch DROP COLUMN runnerid")
"""
"""
a.insert("ALTER TABLE gameData_status ALTER COLUMN statusCode TYPE varchar(3)")
"""
"""
a.insert("ALTER TABLE livedata_plays_pitch ADD COLUMN reviewdetailsreviewtype text")
"""

"""
a.insert("SELECT gameid,COUNT(DISTINCT atbatid) FROM liveData_plays_pitch GROUP BY gameid;")
counter= 0 
for i in a.cur.fetchall():
    print(i)
    counter+=1
print(counter)
"""

#a.insert("ALTER TABLE liveData_linescore ADD COLUMN isWinner BOOLEAN")
#a.insert("ALTER TABLE liveData_plays_pitch ADD COLUMN reviewdetailschallengeteamid integer")
#a.insert("ALTER TABLE liveData_plays_pitch ADD COLUMN reviewdetailsisoverturned boolean")
#a.insert("ALTER TABLE gameData_status ADD COLUMN starttimetbd boolean")
#a.insert("ALTER TABLE liveData_plays_pitch ADD COLUMN pitchdatanastyfactor decimal")
#a.insert("ALTER TABLE gamedata_teams ADD COLUMN parentorgid integer")
"""
a.insert(
SELECT m.gameid,m.atbatid,m.pitcherfullname,m.batterfullname,p.description
FROM livedata_plays_matchup m
JOIN liveData_plays_result p
ON p.gameid = m.gameid AND p.atbatid = m.atbatid
WHERE batterfullName = 'Nolan Arenado' 
ORDER BY gameid,atbatid
)
for i in a.cur.fetchall():
    print(i)
"""

"""
CREATE INDEX ON livedata_plays_runners (runnerid);
"""
"""
CREATE INDEX ON gamedata_players (id);
"""
