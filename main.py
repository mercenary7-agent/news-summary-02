#!/usr/bin/env python3
"""news-summary-01 entry: deterministic one-day world news summary (11 Nov 2026)."""
import sys

SUMMARY = """World in brief — Wednesday, 11 November 2026

1. Iran: Trump declared the war "militarily over" while Hormuz stays closed; mine strikes burned two tankers, Brent +2.4% to $93.69 (Reuters, Yonhap).
2. Ukraine: Abu Dhabi US-Russia-Ukraine talks entered day 2; a POW swap was agreed yet strikes killed 3 in Odesa (Reuters).
3. Indonesia: VP Gibran Rakabuming Raka plans to resign after his education credentials were invalidated; 120 lawmakers moved impeachment (AP).
4. US: the House voted 211-204 to shelve Hegseth impeachment; October CPI rose 0.4% and Fed's Goolsbee called it "borderline disturbing" (Reuters, CNBC).
5. US-China: a "superintelligence" AI dialogue advanced at the Trump-Xi APEC summit in Shenzhen, Nov 18-19 (Reuters).
6. Markets: STOXX 600 hit a record 663.05 (+0.72%), DAX +1.2%, Nasdaq +1.6% to 25,466, S&P +1.31%, CoreWeave +24.7% (Reuters, CNBC).
7. Gaza/Yemen: an Israeli hospital strike in Gaza killed four; Saudi Arabia downed three Houthi missiles over Riyadh (Reuters).
8. Malaysia: ex-PM Najib Razak starts house arrest until Aug 2028 after a royal pardon, with a RM50m 1MDB fine (AP).
9. Europe: Spain saw its first general strike in 14 years; hoax bomb emails hit 300+ Italian schools; a Bulgarian motorway pile-up killed 11; Belarus drones shut Vilnius airport (Reuters, LRT).
10. Africa: DR Congo's Ebola outbreak passed 11,000 cases and 5,387 deaths; Kenya released its last patient; 64,000+ fled floods in Nigeria (AP, UNHCR).
11. World: Pope Leo XIV closed his Argentina tour with a 6m crowd in Peru; at COP31 in Antalya, Iran demanded compensation for strike damage (Reuters).
12. Tech: Nvidia's board weighed ousting CEO Jensen Huang over a China chip-spy report (WSJ); easyJet ordered jets in a £5.7bn deal (Reuters).
13. Business: Thomson Reuters launched a $500m buyback of up to 7m shares amid AI cost worries; the EU advanced a Digital Fairness Act (Reuters).
14. Science: NASA said the 2026 Antarctic ozone hole was the seventh-largest on record (NASA).
"""


def main() -> int:
    text = SUMMARY
    assert 1 <= len(text) <= 2000, f"summary length {len(text)} out of range"
    sys.stdout.write(text)  # deterministic: same bytes on every run
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
