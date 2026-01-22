# FAILURES (10)

Each example below is a misclassification from the eval subset. Failure types are heuristic labels.

## 1) Failure type: Ambiguous / context-dependent
- Text: "Ken Caminiti, 1996 NL MVP, Dies at Age 41 NEW YORK - Ken Caminiti, the 1996 National League MVP who later admitted using steroids during his major league career, died Sunday. He was 41..."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=mid, neg=no_negation, punc=no_punctuation

## 2) Failure type: Length sensitivity
- Text: "Dodgers Nip Giants 3-2 in Crucial Series SAN FRANCISCO - Shawn Green can sit out Saturday knowing he was a huge help to the Dodgers during their crucial series against San Francisco. Green hit a two-run homer in Los Angeles' 3-2 victory over the Giants on Friday night, a day before the first baseman will miss a game to observe the Jewish holiday Yom Kippur..."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=long, neg=no_negation, punc=no_punctuation

## 3) Failure type: Ambiguous / context-dependent
- Text: "Two hurricanes = two deductibles Many homeowners in the Orlando area suffered a double blow when hurricanes Charley and Frances struck in quick succession. Now, they #39;re smarting from a financial one-two punch - two insurance deductibles."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=mid, neg=no_negation, punc=no_punctuation

## 4) Failure type: Length sensitivity
- Text: "Men Set for Sizzling Duel in 100 Meters ATHENS, Greece - The preliminaries in the 100 meters were perhaps just a sample of what's to come Sunday, when a talented group of qualifiers - including Americans Shawn Crawford, Justin Gatlin and defending champion Maurice Greene - will try to turn their competition into the fastest show at the Athens Games.    Five men broke 10 seconds in qualifying Saturday, led by Crawford's time of 9.89..."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=long, neg=no_negation, punc=no_punctuation

## 5) Failure type: Ambiguous / context-dependent
- Text: "Australia establish 300-run lead in third India Test (AFP) AFP - Australia batted cautiously in their second innings to build a lead of 300 runs over India with nine wickets in hand in the third cricket Test here."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=mid, neg=no_negation, punc=no_punctuation

## 6) Failure type: Negation confusion
- Text: "America #39;s curse There is an all but unanswerable case for asserting that the biggest story out of the United States this week has nothing to do with the presidential election, has no connection with the flu vaccine shortage and that it does not involve a gay bishop either"
- True label: Sports
- Predicted: Not Sports
- Slice tags: len=long, neg=negation, punc=no_punctuation

## 7) Failure type: Punctuation / emphasis
- Text: "Special to ESPN.com It #39;s the age old question:  quot;What do you give to the man who #39;s been everything? quot;. Only time will tell whether Phil Knight #39;s retirement will be as long-lived as so many players he paid to endorse Nike."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=long, neg=no_negation, punc=punctuation

## 8) Failure type: Ambiguous / context-dependent
- Text: "Football: Brazil legend's UK debut Brazil football great Socrates is set to make his debut for non-league Garforth Town on Saturday."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=mid, neg=no_negation, punc=no_punctuation

## 9) Failure type: Ambiguous / context-dependent
- Text: "Collingwood anchors England (AFP) AFP - Paul Collingwood's unbeaten 80 took England to 299 for seven against Zimbabwe in their opening Champions Trophy Pool D match at Edgbaston here."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=mid, neg=no_negation, punc=no_punctuation

## 10) Failure type: Ambiguous / context-dependent
- Text: "US edge out Brazil for gold The United States beat Brazil 2-1 in extra time to win the women's Olympic football tournament."
- True label: Not Sports
- Predicted: Sports
- Slice tags: len=mid, neg=no_negation, punc=no_punctuation

