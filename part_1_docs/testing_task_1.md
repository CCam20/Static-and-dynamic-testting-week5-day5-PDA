### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#find 6 issues

  def check_for_ace(self, card):
    if card.value = 1:                        
      return True
    else                                       # : missing 
      return False
   

  dif highest_card(self, card1 card2):         # dif misspelt as def  # , missing between card1 and card2
  if card1.value > card2.value:                # Indent one to far to left on all 4 lines
    return card                                # 1 missing from card1 # Indent missing 
  else:
    return card2
  


def cards_total(self, cards):
  total                                        # total not defined , either empty list or 0
  for card in cards:
    total += card.value
    return "You have a total of" + total       # Needs to be f"You have a total of {total}" # also indented one to many times
  
```
