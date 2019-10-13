p2s2 - Patriots Postgame Stats Scraper
========================================

*This simple script will scrape the data for the most recent patriots game into a 
beautifully formatted markdown table for use with reddit*

**Setup**

*This assumes you have >= Python 3.6 installed*

Navigate to the directory where you downloaded/cloned this repo into, and type the following in your terminal:

**For Ubuntu/Debian**

```
python3 -m pip install -r requirements.txt
```

**For Windows**

```
python -m pip install -r requirements.txt
```

**Use:**

To run the script, navigate to the directory where you downloaded it and type the following:

**For Ubuntu/Debian**

```
python3 p2s2.py
```
**For Windows**

```
python p2s2.py
```

*The json data retrieved for the game doesn't include the full date/time of the game, so after running 
you will be prompted for the date/time.*

**Full example with output**

```
root@dev-environment:/home/dev-environment/Desktop/python_random/p2s2# python3 p2s2.py

Enter game date and time:
10/10/2019 08:20 PM

#New York Giants at New England Patriots

Gillette Stadium - 10/10/2019 08:20 PM Eastern
***

| Team | Q1 | Q2 | Q3 | Q4 | Total |
|:--:|:--:|:--:|:--:|:--:|:--:|
| Giants | 0 | 14 | 0 | 0 | 14 |
| Patriots | 7 | 14 | 0 | 14 | 35 |

**Scoring Plays**


| Team | Quarter | Type | Description |
|:--:|:--:|:--:|:--|
| Patriots | 1 | TD | (1:48) R.Dixon punt is BLOCKED by B.Bolden, Center-Z.DeOssie, RECOVERED by NE-C.Winovich at NYG 6. C.Winovich for 6 yards, TOUCHDOWN. Blocked by credit to NE 38-Bolden. Bolden drives NYG 45-N.Stupar backwards to cause the blocked punt. |
| Patriots | 2 | TD | (7:17) B.Bolden left guard for 1 yard, TOUCHDOWN. |
| Giants | 2 | TD | (6:15) (No Huddle, Shotgun) D.Jones pass deep right to G.Tate for 64 yards, TOUCHDOWN. |
| Giants | 2 | TD | (4:54) (Shotgun) T.Brady sacked at NE 43 for -9 yards (L.Carter). FUMBLES (L.Carter) [L.Carter], RECOVERED by NYG-M.Golden at NE 42. M.Golden for 42 yards, TOUCHDOWN. NE-J.Gordon was injured during the play. His return is Questionable. |
| Patriots | 2 | TD | (:38) J.Eluemunor reported in as eligible.  T.Brady up the middle for 1 yard, TOUCHDOWN. |
| Patriots | 4 | TD | (8:43) (Shotgun) D.Jones pass short right to J.Hilliman to NYG 26 for -7 yards (J.Collins). FUMBLES (J.Collins), RECOVERED by NE-K.Van Noy at NYG 22. K.Van Noy ran ob at NYG 2 for 20 yards (D.Jones). The Replay Official reviewed the runner was out of bounds ruling, and the play was REVERSED. (Shotgun) D.Jones pass short right to J.Hilliman to NYG 26 for -7 yards (J.Collins). FUMBLES (J.Collins), touched at NYG 25, RECOVERED by NE-K.Van Noy at NYG 22. K.Van Noy for 22 yards, TOUCHDOWN. |
| Patriots | 4 | TD | (3:53) T.Brady up the middle for 1 yard, TOUCHDOWN. NE 12-Brady 3rd career 2-TD game |

| Team | Penalties | Rushing Yards | Net Passing Yards | Scrim. Yards| Time of Possession | Turnovers |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| NYG | 5 | 52 | 161 | 213 | 20:24 | 4 |
| NE | 3 | 114 | 313 | 427 | 39:24 | 2 |

```
