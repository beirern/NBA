Win Shares Correlation
================
Nicola Beirer
5/14/2019

Data was provided via Kaggle
<https://www.kaggle.com/drgilermo/nba-players-stats>

The data set stores players stats from players from 1950 to 2017. I will
be using stats for players from 1980-2017 since the 1980’s are the first
decade with the 3 point line. Here are the statistics the data set
provides.

    ##        G               GS              MP            PER       
    ##  Min.   :26.00   Min.   : 0.00   Min.   : 753   Min.   : 4.70  
    ##  1st Qu.:68.00   1st Qu.:10.00   1st Qu.:1260   1st Qu.:11.90  
    ##  Median :77.00   Median :38.00   Median :1829   Median :14.20  
    ##  Mean   :71.97   Mean   :40.23   Mean   :1866   Mean   :14.45  
    ##  3rd Qu.:81.00   3rd Qu.:73.00   3rd Qu.:2450   3rd Qu.:16.60  
    ##  Max.   :84.00   Max.   :83.00   Max.   :3417   Max.   :31.70  
    ##                  NA's   :454                                   
    ##       TS.             X3PAr              FTr              ORB.       
    ##  Min.   :0.3950   Min.   :0.00000   Min.   :0.0570   Min.   : 0.500  
    ##  1st Qu.:0.5040   1st Qu.:0.00400   1st Qu.:0.2420   1st Qu.: 3.500  
    ##  Median :0.5310   Median :0.01300   Median :0.3150   Median : 6.700  
    ##  Mean   :0.5331   Mean   :0.03945   Mean   :0.3325   Mean   : 6.584  
    ##  3rd Qu.:0.5600   3rd Qu.:0.04400   3rd Qu.:0.4020   3rd Qu.: 9.100  
    ##  Max.   :0.7020   Max.   :0.56000   Max.   :0.8670   Max.   :19.600  
    ##                                                                      
    ##       DRB.            TRB.             AST.             STL.      
    ##  Min.   : 3.00   Min.   : 2.400   Min.   : 0.900   Min.   :0.200  
    ##  1st Qu.: 7.70   1st Qu.: 5.700   1st Qu.: 7.975   1st Qu.:1.200  
    ##  Median :12.40   Median : 9.800   Median :12.250   Median :1.600  
    ##  Mean   :13.28   Mean   : 9.929   Mean   :14.594   Mean   :1.706  
    ##  3rd Qu.:18.30   3rd Qu.:13.600   3rd Qu.:19.800   3rd Qu.:2.100  
    ##  Max.   :33.80   Max.   :23.000   Max.   :54.800   Max.   :5.600  
    ##                                                                   
    ##       BLK.             TOV.            USG.            OWS        
    ##  Min.   : 0.000   Min.   : 5.60   Min.   : 5.20   Min.   :-2.700  
    ##  1st Qu.: 0.400   1st Qu.:12.50   1st Qu.:16.20   1st Qu.: 0.500  
    ##  Median : 0.800   Median :15.10   Median :19.30   Median : 1.500  
    ##  Mean   : 1.258   Mean   :15.45   Mean   :19.47   Mean   : 2.084  
    ##  3rd Qu.: 1.700   3rd Qu.:17.90   3rd Qu.:22.60   3rd Qu.: 3.200  
    ##  Max.   :10.800   Max.   :34.80   Max.   :38.30   Max.   :15.200  
    ##                                                                   
    ##       DWS               WS             WS.48               OBPM        
    ##  Min.   :-0.200   Min.   :-1.400   Min.   :-0.09100   Min.   :-7.0000  
    ##  1st Qu.: 1.000   1st Qu.: 1.800   1st Qu.: 0.06400   1st Qu.:-1.8000  
    ##  Median : 1.700   Median : 3.300   Median : 0.09200   Median :-0.5000  
    ##  Mean   : 1.922   Mean   : 4.006   Mean   : 0.09406   Mean   :-0.3181  
    ##  3rd Qu.: 2.600   3rd Qu.: 5.600   3rd Qu.: 0.12100   3rd Qu.: 1.0000  
    ##  Max.   : 7.800   Max.   :21.200   Max.   : 0.30800   Max.   : 9.8000  
    ##                                                                        
    ##       DBPM               BPM               VORP              FG        
    ##  Min.   :-5.90000   Min.   :-8.2000   Min.   :-1.900   Min.   :  40.0  
    ##  1st Qu.:-1.20000   1st Qu.:-2.1000   1st Qu.: 0.000   1st Qu.: 188.0  
    ##  Median :-0.20000   Median :-0.5000   Median : 0.600   Median : 297.0  
    ##  Mean   :-0.05446   Mean   :-0.3731   Mean   : 1.037   Mean   : 336.9  
    ##  3rd Qu.: 1.10000   3rd Qu.: 1.2000   3rd Qu.: 1.800   3rd Qu.: 453.2  
    ##  Max.   : 6.50000   Max.   :12.6000   Max.   :12.000   Max.   :1098.0  
    ##                                                                        
    ##       FGA              FG.              X3P              X3PA       
    ##  Min.   :  79.0   Min.   :0.3010   Min.   :  0.00   Min.   :  0.00  
    ##  1st Qu.: 394.0   1st Qu.:0.4550   1st Qu.:  0.00   1st Qu.:  2.00  
    ##  Median : 616.5   Median :0.4790   Median :  1.00   Median :  8.00  
    ##  Mean   : 691.1   Mean   :0.4825   Mean   :  7.91   Mean   : 26.95  
    ##  3rd Qu.: 918.2   3rd Qu.:0.5090   3rd Qu.:  7.00   3rd Qu.: 30.00  
    ##  Max.   :2279.0   Max.   :0.6700   Max.   :166.00   Max.   :466.00  
    ##                                                                     
    ##       X3P.             X2P            X2PA             X2P.       
    ##  Min.   :0.0000   Min.   :  39   Min.   :  78.0   Min.   :0.3280  
    ##  1st Qu.:0.0000   1st Qu.: 182   1st Qu.: 377.8   1st Qu.:0.4630  
    ##  Median :0.1890   Median : 288   Median : 587.0   Median :0.4870  
    ##  Mean   :0.1814   Mean   : 329   Mean   : 664.1   Mean   :0.4899  
    ##  3rd Qu.:0.3000   3rd Qu.: 442   3rd Qu.: 884.0   3rd Qu.:0.5150  
    ##  Max.   :1.0000   Max.   :1086   Max.   :2213.0   Max.   :0.6700  
    ##  NA's   :229                                                      
    ##       eFG.              FT             FTA             FT.        
    ##  Min.   :0.3050   Min.   :  7.0   Min.   : 19.0   Min.   :0.3100  
    ##  1st Qu.:0.4607   1st Qu.: 86.0   1st Qu.:118.8   1st Qu.:0.7070  
    ##  Median :0.4860   Median :141.0   Median :189.0   Median :0.7630  
    ##  Mean   :0.4882   Mean   :172.3   Mean   :226.5   Mean   :0.7514  
    ##  3rd Qu.:0.5140   3rd Qu.:230.0   3rd Qu.:299.2   3rd Qu.:0.8110  
    ##  Max.   :0.6700   Max.   :833.0   Max.   :972.0   Max.   :0.9580  
    ##                                                                   
    ##       ORB             DRB             TRB              AST         
    ##  Min.   :  5.0   Min.   : 29.0   Min.   :  43.0   Min.   :  11.00  
    ##  1st Qu.: 55.0   1st Qu.:118.0   1st Qu.: 177.0   1st Qu.:  88.75  
    ##  Median : 95.0   Median :184.0   Median : 275.5   Median : 156.50  
    ##  Mean   :111.6   Mean   :227.4   Mean   : 339.0   Mean   : 200.93  
    ##  3rd Qu.:156.0   3rd Qu.:306.0   3rd Qu.: 464.0   3rd Qu.: 259.25  
    ##  Max.   :573.0   Max.   :864.0   Max.   :1216.0   Max.   :1128.00  
    ##                                                                    
    ##       STL              BLK              TOV              PF       
    ##  Min.   :  8.00   Min.   :  0.00   Min.   : 25.0   Min.   : 35.0  
    ##  1st Qu.: 38.00   1st Qu.: 11.00   1st Qu.: 84.0   1st Qu.:140.0  
    ##  Median : 59.50   Median : 25.00   Median :127.0   Median :188.0  
    ##  Mean   : 67.86   Mean   : 41.75   Mean   :135.8   Mean   :188.7  
    ##  3rd Qu.: 88.00   3rd Qu.: 55.00   3rd Qu.:177.0   3rd Qu.:235.0  
    ##  Max.   :301.00   Max.   :456.00   Max.   :359.0   Max.   :386.0  
    ##                                                                   
    ##       PTS        
    ##  Min.   : 107.0  
    ##  1st Qu.: 470.0  
    ##  Median : 748.5  
    ##  Mean   : 854.1  
    ##  3rd Qu.:1151.0  
    ##  Max.   :3041.0  
    ## 

As you can see there are many stats here, from box score stats to
advanced. I have filtered out players who have played less than 25 games
and less than 750 minutes (\~30 MPG) for the season. I have also split
the data into decades (1980s, 1990s, 2000s, 2010-2017).

Now I will loop through all variables and see corrolation between them
and Win Shares

Obviously there is a lot to see, we’ll loop through all variables and
see corrolation between them and Win Shares, print only when corrolation
\> .5

    ## [1] "GS  est: 0.661961899400077  p=value: 1.08319211684078e-245"
    ## [1] "MP  est: 0.794050777901544  p=value: 0"
    ## [1] "PER  est: 0.830827244537251  p=value: 0"
    ## [1] "TS.  est: 0.628445791554578  p=value: 6.11250425699388e-264"
    ## [1] "OWS  est: 0.935749470977172  p=value: 0"
    ## [1] "DWS  est: 0.711544828929812  p=value: 0"
    ## [1] "WS  est: 1  p=value: 0"
    ## [1] "WS.48  est: 0.890837041985755  p=value: 0"
    ## [1] "OBPM  est: 0.816975311050281  p=value: 0"
    ## [1] "BPM  est: 0.829597097284534  p=value: 0"
    ## [1] "VORP  est: 0.903225223700358  p=value: 0"
    ## [1] "FG  est: 0.782518869643077  p=value: 0"
    ## [1] "FGA  est: 0.723275225019147  p=value: 0"
    ## [1] "FG.  est: 0.526306030258321  p=value: 3.96727862005505e-171"
    ## [1] "X2P  est: 0.779057073092728  p=value: 0"
    ## [1] "X2PA  est: 0.722295992117066  p=value: 0"
    ## [1] "X2P.  est: 0.54262251873529  p=value: 7.41036783194679e-184"
    ## [1] "eFG.  est: 0.541899679717868  p=value: 2.80967946968725e-183"
    ## [1] "FT  est: 0.810014792076484  p=value: 0"
    ## [1] "FTA  est: 0.79722374783629  p=value: 0"
    ## [1] "ORB  est: 0.56614842933851  p=value: 1.71947166824197e-203"
    ## [1] "DRB  est: 0.599604918512341  p=value: 2.6855885343463e-234"
    ## [1] "TRB  est: 0.608193953865498  p=value: 8.31153162203453e-243"
    ## [1] "STL  est: 0.545180348731036  p=value: 6.46042835942494e-186"
    ## [1] "TOV  est: 0.644557552422549  p=value: 6.57168396789102e-282"
    ## [1] "PTS  est: 0.813959800607271  p=value: 0"

Do this for the other Decades

    ## [1] "GS  est: 0.627308131194847  p=value: 1.82908997607387e-303"
    ## [1] "MP  est: 0.759647078071606  p=value: 0"
    ## [1] "PER  est: 0.793353635361703  p=value: 0"
    ## [1] "TS.  est: 0.609761263197331  p=value: 2.81417836035051e-282"
    ## [1] "OWS  est: 0.938216692121426  p=value: 0"
    ## [1] "DWS  est: 0.777289992729993  p=value: 0"
    ## [1] "WS  est: 1  p=value: 0"
    ## [1] "WS.48  est: 0.860820968121063  p=value: 0"
    ## [1] "OBPM  est: 0.75062364935834  p=value: 0"
    ## [1] "BPM  est: 0.832364921466119  p=value: 0"
    ## [1] "VORP  est: 0.915921244350856  p=value: 0"
    ## [1] "FG  est: 0.758276881327336  p=value: 0"
    ## [1] "FGA  est: 0.698704012271708  p=value: 0"
    ## [1] "X2P  est: 0.717213162994774  p=value: 0"
    ## [1] "X2PA  est: 0.663537768534727  p=value: 0"
    ## [1] "X2P.  est: 0.501573704593411  p=value: 9.66663093759762e-177"
    ## [1] "eFG.  est: 0.520548047344936  p=value: 1.44483994641672e-192"
    ## [1] "FT  est: 0.772138068156372  p=value: 0"
    ## [1] "FTA  est: 0.764555137342554  p=value: 0"
    ## [1] "DRB  est: 0.620254189394116  p=value: 8.74340486017014e-295"
    ## [1] "TRB  est: 0.583691159052204  p=value: 3.7744567403389e-253"
    ## [1] "STL  est: 0.612480189867415  p=value: 1.79286137414659e-285"
    ## [1] "TOV  est: 0.618797361507283  p=value: 5.08935312558898e-293"
    ## [1] "PTS  est: 0.788067618360781  p=value: 0"

    ## [1] "GS  est: 0.638558075353015  p=value: 0"
    ## [1] "MP  est: 0.767934260064065  p=value: 0"
    ## [1] "PER  est: 0.813447388001418  p=value: 0"
    ## [1] "TS.  est: 0.577387033010931  p=value: 3.59619389308373e-274"
    ## [1] "OWS  est: 0.934894746860199  p=value: 0"
    ## [1] "DWS  est: 0.741331395009258  p=value: 0"
    ## [1] "WS  est: 1  p=value: 0"
    ## [1] "WS.48  est: 0.861446896005257  p=value: 0"
    ## [1] "OBPM  est: 0.747986112711736  p=value: 0"
    ## [1] "BPM  est: 0.843188258199103  p=value: 0"
    ## [1] "VORP  est: 0.918671453447015  p=value: 0"
    ## [1] "FG  est: 0.779182705411531  p=value: 0"
    ## [1] "FGA  est: 0.718253869233977  p=value: 0"
    ## [1] "X2P  est: 0.740910179859731  p=value: 0"
    ## [1] "X2PA  est: 0.694871404270289  p=value: 0"
    ## [1] "FT  est: 0.764723173044525  p=value: 0"
    ## [1] "FTA  est: 0.756596715538044  p=value: 0"
    ## [1] "DRB  est: 0.686036336180995  p=value: 0"
    ## [1] "TRB  est: 0.637451825848822  p=value: 0"
    ## [1] "AST  est: 0.50381863147353  p=value: 1.50204512747125e-198"
    ## [1] "STL  est: 0.596163566873505  p=value: 1.0224892546132e-296"
    ## [1] "TOV  est: 0.609321417029102  p=value: 1.98956768069466e-313"
    ## [1] "PTS  est: 0.796350538115085  p=value: 0"

    ## [1] "GS  est: 0.600702898602723  p=value: 3.9036457806487e-258"
    ## [1] "MP  est: 0.722968457161565  p=value: 0"
    ## [1] "PER  est: 0.793984425996305  p=value: 0"
    ## [1] "TS.  est: 0.596332612124016  p=value: 1.79261679219955e-253"
    ## [1] "OWS  est: 0.941873647874699  p=value: 0"
    ## [1] "DWS  est: 0.758978350518596  p=value: 0"
    ## [1] "WS  est: 1  p=value: 0"
    ## [1] "WS.48  est: 0.865095704135147  p=value: 0"
    ## [1] "OBPM  est: 0.719122190973441  p=value: 0"
    ## [1] "BPM  est: 0.830562321549507  p=value: 0"
    ## [1] "VORP  est: 0.908320616158419  p=value: 0"
    ## [1] "FG  est: 0.760894615717384  p=value: 0"
    ## [1] "FGA  est: 0.677073037499423  p=value: 0"
    ## [1] "X2P  est: 0.715321673758133  p=value: 0"
    ## [1] "X2PA  est: 0.656701869976424  p=value: 0"
    ## [1] "FT  est: 0.744160744530011  p=value: 0"
    ## [1] "FTA  est: 0.748313248215207  p=value: 0"
    ## [1] "DRB  est: 0.678090894243695  p=value: 0"
    ## [1] "TRB  est: 0.638954222048427  p=value: 3.22058923376336e-302"
    ## [1] "STL  est: 0.554232937727743  p=value: 5.11666069418479e-212"
    ## [1] "TOV  est: 0.584961476065377  p=value: 1.13053220253409e-241"
    ## [1] "PTS  est: 0.775436538889244  p=value: 0"

Most of the data is rather unsurprising. Though looking at the first
table surprised me as some of the stats that I thought would corrolate
with Win Shares ended up showing weak corrolation. One thing to note is
that all the data has been filtered, everyone has played more than **25
Games** each season and around **30 minutes a game** on average. This
would explain why Games, Games Starting, and Minutes played have a lower
corrolation that might be expected, while the data is skewed left all
the data is full of players who play a good amount of games and minutes,
obviously playing more games gives you a greater chance at win shares
when comparing 1 game to 30, but all these guys play a good amount of
games.

One thing I found surprised is that *3PAr and 3P% had such a low and
even a negative corrolation to Win Shares*. While the data is only for
the 1980s when 3 point shooting was not as popular as it is now, it is
still surprising to see a negative corrolation with the most valuable
shot in the game. This also shows that *players can contribute to team
success in more ways that just shooting, even though it seems that the
best player a team can get is a “3 and D” guy*. My conjecture for the
weak 3 Point corrolation is that individuals do not have to shoot 3s to
help their team win but a team must shoot well from 3 to be sucessful
and have championship aspirations, this is just a conjecture and
something to test.

Another surprising thing was the low corrolation between *Assists* and
Win Shares and *Rebounds* and Win Shares. I have the same theory with
these stats that I had with 3 Point Shooting, **one individual** does
not need to be an amazing 3 point shooter, high assister, or a monster
rebounder, but a **team** as a whole must do these things well. It seems
like the best teams now are the best 3 point and assist teams. I’ll be
analyzing team statistics later and this is what I’ll be looking at
next.

One interesting thing is that the corrolation between *MP has decreased
and is below 0.5 since 2010*. One NBA commentator, I believe it was Greg
Anthony, said that he feels that the modern game is able to utilize more
players better and get the whole bench involved. While this is
anecdotal, it is interesting to note that the corrolation with MP has
decreased and seems to back up that claim. Again, all data is filtered
to be players aove 750 minutes a season or 30 minutes a games so players
get a good amount of minutes but it does seem to suggest that *Win
Shares can be obtained by bench players who get good minutes*.
