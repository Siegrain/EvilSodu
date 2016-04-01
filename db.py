import random


def get(type):
    if type == 'quote':
        return random.choice(QUOTES.split('\n'))
    elif type == 'yesno':
        return random.choice(['Yes.', 'Probably.', 'Maybe.', 'No.'])
    elif type == 'when':
        return random.choice(['In a few days.',
                              'In a few weeks.',
                              'In a few months.',
                              'In a few years.',
                              'Never.'])
    elif type == 'bane':
        return random.choice(BANE_QUOTES.split('\n'))
    elif type == 'joke':
        return random.choice(JOKES.split('\n'))
    elif type == 'cat':
        return random.choice(CATS)
    elif type == 'doge':
        return random.choice(SHIBA_DOG)
    elif type == 'book':
        return random.choice(BOOKS)
    elif type == 'necro':
        return random.choice(NECRONOMICON.split('\n'))
    elif type == 'song':
        return random.choice(SONGS.split('\n'))
    elif type == 'crowley':
        return '>inb4 GD\'s hate parade on his grave'
    elif type == 'thoth':
        return '>Thoth: The current sexuality movement, along with the inability to accept facts, will be the downfall of our modern day Rome.'


def get_card(deck, type):
    if type == 'single':
        if deck == 'rw':
            return random.choice(RW_DECK)
        elif deck == 'thoth':
            return random.choice(THOTH_DECK)
    elif type == 'spread':
        if deck == 'rw':
            return ' / '.join(random.sample(RW_DECK, 3))
        elif deck == 'thoth':
            return ' / '.join(random.sample(THOTH_DECK, 3))


def get_rune(type):
    if type == 'single':
        return random.choice(RUNES)
    elif type == 'spread':
        return ' / '.join(random.sample(RUNES, 3))

# ----------------------------------------------------------------------------

# Album: http://imgur.com/a/zBwe3
RW_DECK = [
    "0 - The Fool { http://i.imgur.com/xwIpqIC.jpg }",
    "I - The Magician { http://i.imgur.com/mxJtSKd.jpg }",
    "II - The High Priestess { http://i.imgur.com/d764bKL.jpg }",
    "III - The Empress { http://i.imgur.com/BVMYp3Z.jpg }",
    "IV - The Emperor { http://i.imgur.com/VxmSea8.jpg }",
    "V - The Hierophant { http://i.imgur.com/VbHYvph.jpg }",
    "VI - The Lovers { http://i.imgur.com/lwsa3LM.jpg }",
    "VII - The Chariot { http://i.imgur.com/LRMtkTi.jpg }",
    "VIII - Strength { http://i.imgur.com/rtUPtsZ.jpg }",
    "IX - The Hermit { http://i.imgur.com/BJVCRmh.jpg }",
    "X - Wheel of Fortune { http://i.imgur.com/TEceoge.jpg }",
    "XI - Justice { http://i.imgur.com/xaNM3PW.jpg }",
    "XII - The Hanged Man { http://i.imgur.com/XL6jhjQ.jpg }",
    "XIII - Death { http://i.imgur.com/vN8frAu.jpg }",
    "XIV - Temperance { http://i.imgur.com/b1g6FlS.jpg }",
    "XV - The Devil { http://i.imgur.com/ppC8WVB.jpg }",
    "XVI - The Tower { http://i.imgur.com/aBv2lbO.jpg }",
    "XVII - The Star { http://i.imgur.com/S3WZmhm.jpg }",
    "XVIII - The Moon { http://i.imgur.com/oZtqyCr.jpg }",
    "XIX - The Sun { http://i.imgur.com/dalzqXX.jpg }",
    "XX - Judgement { http://i.imgur.com/1DrOwqp.jpg }",
    "XXI - The World { http://i.imgur.com/aRGuRFG.jpg }",
    "Ace of Wands { http://i.imgur.com/DabavYD.jpg }",
    "2 of Wands { http://i.imgur.com/BMU6WWF.jpg }",
    "3 of Wands { http://i.imgur.com/GLj7gSc.jpg }",
    "4 of Wands { http://i.imgur.com/UPqeaU3.jpg }",
    "5 of Wands { http://i.imgur.com/8bayVFQ.jpg }",
    "6 of Wands { http://i.imgur.com/y2PDGpt.jpg }",
    "7 of Wands { http://i.imgur.com/vEbIZC5.jpg }",
    "8 of Wands { http://i.imgur.com/63Gs9p7.jpg }",
    "9 of Wands { http://i.imgur.com/DK5D6WT.jpg }",
    "10 of Wands { http://i.imgur.com/BFKf1UI.jpg }",
    "King of Wands { http://i.imgur.com/TC4ulvh.jpg }",
    "Queen of Wands { http://i.imgur.com/qW1mEme.jpg }",
    "Knight of Wands { http://i.imgur.com/e6KDbgR.jpg }",
    "Page of Wands { http://i.imgur.com/Yd2jSck.jpg }",
    "Ace of Cups { http://i.imgur.com/C7tqudR.jpg }",
    "2 of Cups { http://i.imgur.com/lRYMKvv.jpg }",
    "3 of Cups { http://i.imgur.com/k3OOClg.jpg }",
    "4 of Cups { http://i.imgur.com/5a9PJMq.jpg }",
    "5 of Cups { http://i.imgur.com/CCqnB7K.jpg }",
    "6 of Cups { http://i.imgur.com/6EYsVJI.jpg }",
    "7 of Cups { http://i.imgur.com/eKoqpps.jpg }",
    "8 of Cups { http://i.imgur.com/e4Ga7nE.jpg }",
    "9 of Cups { http://i.imgur.com/l4Ws2gO.jpg }",
    "10 of Cups { http://i.imgur.com/dCgX4Ia.jpg }",
    "King of Cups { http://i.imgur.com/kva3dt9.jpg }",
    "Queen of Cups { http://i.imgur.com/kJtgSAQ.jpg }",
    "Knight of Cups { http://i.imgur.com/uqqqLUq.jpg }",
    "Page of Cups { http://i.imgur.com/UUR02Qn.jpg }",
    "Ace of Swords { http://i.imgur.com/WnHJVUz.jpg }",
    "2 of Swords { http://i.imgur.com/hbeuU1m.jpg }",
    "3 of Swords { http://i.imgur.com/Ut69sBV.jpg }",
    "4 of Swords { http://i.imgur.com/2jHpfqL.jpg }",
    "5 of Swords { http://i.imgur.com/iWeFBUh.jpg }",
    "6 of Swords { http://i.imgur.com/nGvrP0t.jpg }",
    "7 of Swords { http://i.imgur.com/wOHMCCj.jpg }",
    "8 of Swords { http://i.imgur.com/EvRHCRT.jpg }",
    "9 of Swords { http://i.imgur.com/XBpVh02.jpg }",
    "10 of Swords { http://i.imgur.com/zv74MLW.jpg }",
    "King of Swords { http://i.imgur.com/OqVhsfE.jpg }",
    "Queen of Swords { http://i.imgur.com/6ztXVin.jpg }",
    "Knight of Swords { http://i.imgur.com/sJfwrdN.jpg }",
    "Page of Swords { http://i.imgur.com/qO0XgXa.jpg }",
    "Ace of Pentacles { http://i.imgur.com/3mglLg1.jpg }",
    "2 of Pentacles { http://i.imgur.com/RQORVBu.jpg }",
    "3 of Pentacles { http://i.imgur.com/ubGCBP8.jpg }",
    "4 of Pentacles { http://i.imgur.com/rx0nXma.jpg }",
    "5 of Pentacles { http://i.imgur.com/SxOpbH1.jpg }",
    "6 of Pentacles { http://i.imgur.com/izANDOZ.jpg }",
    "7 of Pentacles { http://i.imgur.com/Y180oId.jpg }",
    "8 of Pentacles { http://i.imgur.com/AikIqPX.jpg }",
    "9 of Pentacles { http://i.imgur.com/aadANyr.jpg }",
    "10 of Pentacles { http://i.imgur.com/5W91m6C.jpg }",
    "King of Pentacles { http://i.imgur.com/In9i1FZ.jpg }",
    "Queen of Pentacles { http://i.imgur.com/55RpqQY.jpg }",
    "Knight of Pentacles { http://i.imgur.com/p1291Jn.jpg }",
    "Page of Pentacles { http://i.imgur.com/xxPXOML.jpg }"
]

# Album: http://imgur.com/a/24ByN
THOTH_DECK = [
    "0 - The Fool { http://i.imgur.com/PQ2nG95.jpg }",
    "I - The Magus { http://i.imgur.com/qItZSaz.jpg }",
    "II - The Priestess { http://i.imgur.com/joRLHGK.jpg }",
    "III - The Empress { http://i.imgur.com/1xiJAUq.jpg }",
    "IV - The Emperor { http://i.imgur.com/yVKoH2j.jpg }",
    "V - The Hierophant { http://i.imgur.com/8q8wkZv.jpg }",
    "VI - The Lovers { http://i.imgur.com/7fBAtUv.jpg }",
    "VII - The Chariot { http://i.imgur.com/axTt8o6.jpg }",
    "VIII - Adjustment { http://i.imgur.com/jFK0rW9.jpg }",
    "IX - The Hermit { http://i.imgur.com/vKjpFv6.jpg }",
    "X - Fortune { http://i.imgur.com/SfcEUFi.jpg }",
    "XI - Lust { http://i.imgur.com/pybCauK.jpg }",
    "XII - The Hanged Man { http://i.imgur.com/NH0vt4j.jpg }",
    "XIII - Death { http://i.imgur.com/0RG898u.jpg }",
    "XIV - Art { http://i.imgur.com/G91EXFL.jpg }",
    "XV - The Devil { http://i.imgur.com/RnRASpz.jpg }",
    "XVI - The Tower { http://i.imgur.com/S6Z2f1f.jpg }",
    "XVII - The Star { http://i.imgur.com/3yYIGvm.jpg }",
    "XVIII - The Moon { http://i.imgur.com/wECfVYO.jpg }",
    "XIX - The Sun { http://i.imgur.com/NGwTuoK.jpg }",
    "XX - The Aeon { http://i.imgur.com/LhXJy0f.jpg }",
    "XXI - The Universe { http://i.imgur.com/HDwUWBF.jpg }",
    "Ace of Wands { http://i.imgur.com/UK2efBo.jpg }",
    "2 of Wands - Dominion { http://i.imgur.com/fbzFflB.jpg }",
    "3 of Wands - Virtue { http://i.imgur.com/DwU6See.jpg }",
    "4 of Wands - Completion { http://i.imgur.com/LiMx96X.jpg }",
    "5 of Wands - Strife { http://i.imgur.com/rPlrbyT.jpg }",
    "6 of Wands - Victory { http://i.imgur.com/YyB5fCr.jpg }",
    "7 of Wands - Valour { http://i.imgur.com/nE0HLRN.jpg }",
    "8 of Wands - Swiftness { http://i.imgur.com/ChFeclc.jpg }",
    "9 of Wands - Strength { http://i.imgur.com/wEod3NT.jpg }",
    "10 of Wands - Oppression { http://i.imgur.com/QipWoV0.jpg }",
    "Knight of Wands { http://i.imgur.com/sDVt9RW.jpg }",
    "Queen of Wands { http://i.imgur.com/cL17LkX.jpg }",
    "Prince of Wands { http://i.imgur.com/mB468fd.jpg }",
    "Princess of Wands { http://i.imgur.com/XMO3bNF.jpg }",
    "Ace of Cups { http://i.imgur.com/qm5f07V.jpg }",
    "2 of Cups - Love { http://i.imgur.com/AsweI48.jpg }",
    "3 of Cups - Abundance { http://i.imgur.com/wzQVmtq.jpg }",
    "4 of Cups - Luxury { http://i.imgur.com/ONZVO0P.jpg }",
    "5 of Cups - Disappointment { http://i.imgur.com/xvuIqvn.jpg }",
    "6 of Cups - Pleasure { http://i.imgur.com/Od1qfVh.jpg }",
    "7 of Cups - Debauch { http://i.imgur.com/h2F7eFh.jpg }",
    "8 of Cups - Indolence { http://i.imgur.com/PxdiTDy.jpg }",
    "9 of Cups - Happiness { http://i.imgur.com/JLGko7R.jpg }",
    "10 of Cups - Satiety { http://i.imgur.com/Wmm2lQL.jpg }",
    "Knight of Cups { http://i.imgur.com/rbQZuJ0.jpg }",
    "Queen of Cups { http://i.imgur.com/WdvOb9X.jpg }",
    "Prince of Cups { http://i.imgur.com/CqfClbW.jpg }",
    "Princess of Cups { http://i.imgur.com/BsgXCEO.jpg }",
    "Ace of Swords { http://i.imgur.com/nbGXZMt.jpg }",
    "2 of Swords - Peace { http://i.imgur.com/kpwBVKZ.jpg }",
    "3 of Swords - Sorrow { http://i.imgur.com/0z9d1hY.jpg }",
    "4 of Swords - Truce { http://i.imgur.com/9LNCSNC.jpg }",
    "5 of Swords - Defeat { http://i.imgur.com/Gub5DXA.jpg }",
    "6 of Swords - Science { http://i.imgur.com/etB8X8E.jpg }",
    "7 of Swords - Futility { http://i.imgur.com/gk1ivXT.jpg }",
    "8 of Swords - Interference { http://i.imgur.com/8eXSUQj.jpg }",
    "9 of Swords - Cruelty { http://i.imgur.com/eRQ4XX4.jpg }",
    "10 of Swords - Ruin { http://i.imgur.com/6E4h4d4.jpg }",
    "Knight of Swords { http://i.imgur.com/YZIa5um.jpg }",
    "Queen of Swords { http://i.imgur.com/hb0bjIQ.jpg }",
    "Prince of Swords { http://i.imgur.com/U8CHSV9.jpg }",
    "Princess of Swords { http://i.imgur.com/tfJ2Uu8.jpg }",
    "Ace of Disks { http://i.imgur.com/6FszJp0.jpg }",
    "2 of Disks - Change { http://i.imgur.com/TC3Z0dv.jpg }",
    "3 of Disks - Works { http://i.imgur.com/ZRYRFoQ.jpg }",
    "4 of Disks - Power { http://i.imgur.com/pDi6yuu.jpg }",
    "5 of Disks - Worry { http://i.imgur.com/pEtyIqx.jpg }",
    "6 of Disks - Success { http://i.imgur.com/M2HXS5A.jpg }",
    "7 of Disks - Failure { http://i.imgur.com/ApPSuWl.jpg }",
    "8 of Disks - Prudence { http://i.imgur.com/wg2g8gu.jpg }",
    "9 of Disks - Gain { http://i.imgur.com/mEAyRq2.jpg }",
    "10 of Disks - Wealth { http://i.imgur.com/Z3B5V5E.jpg }",
    "Knight of Disks { http://i.imgur.com/iseQPhE.jpg }",
    "Queen of Disks { http://i.imgur.com/NNi2jMu.jpg }",
    "Prince of Disks { http://i.imgur.com/9CQeGof.jpg }",
    "Princess of Disks { http://i.imgur.com/i2lye5C.jpg }"
]

# Album: https://imgur.com/a/W3cmH
RUNES = [
    "Fehu { https://i.imgur.com/SjPESEW.gif }",
    "Uruz { https://i.imgur.com/KBSvslk.gif }",
    "Thurisaz { https://i.imgur.com/AFUYbye.gif }",
    "Ansuz { https://i.imgur.com/Ps05ytE.gif }",
    "Raidho { https://i.imgur.com/x5kG79B.gif }",
    "Kenaz { https://i.imgur.com/wW5SpF0.gif }",
    "Gebo { https://i.imgur.com/ELL6KSL.gif }",
    "Wunjo { https://i.imgur.com/c8c5M8M.gif }",
    "Hagalaz { https://i.imgur.com/Ni8tUul.gif }",
    "Nauthiz { https://i.imgur.com/hUQGqft.gif }",
    "Isa { https://i.imgur.com/NlDSgTT.gif }",
    "Jera { https://i.imgur.com/lE2QZAN.gif }",
    "Eihwaz { https://i.imgur.com/vGOO917.gif }",
    "Perthro { https://i.imgur.com/NCWTCWT.gif }",
    "Algiz { https://i.imgur.com/e6yy8EK.gif }",
    "Sowilo { https://i.imgur.com/0cW16RB.gif }",
    "Tiwaz { https://i.imgur.com/XD91cMh.gif }",
    "Berkano { https://i.imgur.com/emH7iXn.gif }",
    "Ehwaz { https://i.imgur.com/flRhgtH.gif }",
    "Mannaz { https://i.imgur.com/KQXLM3A.gif }",
    "Laguz { https://i.imgur.com/EUdAkUA.gif }",
    "Ingwaz { https://i.imgur.com/D9jOPSz.gif }",
    "Dagaz { https://i.imgur.com/DwbJt9c.gif }",
    "Othala { https://i.imgur.com/Z2yyPkW.gif }"
]

CATS = [
    "https://i.imgur.com/MQtdUNY.jpg",
    "https://i.imgur.com/0lWg9WQ.jpg",
    "https://i.imgur.com/8GSaMFl.jpg",
    "https://i.imgur.com/3imUiCT.jpg",
    "https://i.imgur.com/levMH6V.jpg",
    "https://i.imgur.com/ZcC2zxh.jpg",
    "https://i.imgur.com/Bqtq2fF.jpg",
    "https://i.imgur.com/28QNXys.jpg",
    "https://i.imgur.com/YxLBe7w.jpg",
    "https://i.imgur.com/rrANafw.jpg",
    "https://i.imgur.com/UFJTGGe.jpg",
    "https://i.imgur.com/ek36vYP.png",
    "https://i.imgur.com/DW7JUCk.jpg",
    "http://i.imgur.com/Zk1P3.png",
    "http://i.imgur.com/e1IRQRr.gif",
    "https://i.imgur.com/prnkyR6.jpg"
]

SHIBA_DOG = [
    "https://i.imgur.com/0daLJG7.jpg",
    "https://i.imgur.com/TOldsqH.jpg",
    "https://i.imgur.com/v2kELhX.png",
    "https://i.imgur.com/3iv2Fal.jpg",
    "https://i.imgur.com/ugP8dVP.jpg",
    "https://i.imgur.com/lotvvU8.jpg",
    "https://i.imgur.com/yA7QGkk.jpg",
    "https://i.imgur.com/gWix15w.jpg",
    "https://i.imgur.com/ccfiImq.jpg",
    "https://i.imgur.com/lgf6T4R.jpg"
]

BOOKS = [
    "Mein Kampf - Adolf Hitler { http://www.greatwar.nl/books/meinkampf/meinkampf.pdf }",
    "Protocols of the Elders of Zion { http://xroads.virginia.edu/~ma01/Kidd/thesis/pdf/protocols.pdf }"
]

QUOTES = '''"Atheists never progress." - Herod, IRCer
"The workers have nothing to lose but their chains." - Karl Marx 
"Don't get got." - Anonymous
"Those people who think they know everything are a great annoyance to those of us who do." - Isaac Asimov 
"Computers are useless. They can only give you answers." - Pablo Picasso 
"They don't think it be like it is, but it do." - Oscar Gamble 
"The mind is not a vessel to be filled but a fire to be kindled." - Plutarch 
"What is missed out is always the best, what is lost is always the most precious." - Anonymous
"Do what thou wilt shall be the whole of the law." - Crowley 
"Man is the lowest-cost, 150-pound, nonlinear, all-purpose computer system which can be mass-produced by unskilled labor." - NASA, 1965 
"It is no measure of health to be well adjusted to a profoundly sick society." - Jiddu Krishnamurti 
"Empty your cup so that it may be filled; become devoid to gain totality." - Bruce Lee 
"Don't boast of tomorrow, for you know not what a day will bring." - Jewish Proverb 
"Now I am quietly waiting for the catastrophe of my personality to seem beautiful again, and interesting, and modern." - Meditations in an Emergency 
"Only those who will risk going too far can possibly find out how far one can go." - T. S. Eliot 
"What power is it that supports our battle yet starves our victory?" - Commander Kang 
"I am committed to whatever the hell it is that you people do around here." - Master Shake 
"I have no special talent. I am only passionately curious."  - Albert Einstein 
"Do not go where the path may lead, go instead where there is no path and leave a trail." - Ralph Waldo Emerson 
"Whenever you find yourself on the side of the majority, it is time to pause and reflect." -Mark Twain 
"Wanting to be someone else is a waste of who you are." - Kurt Cobain 
"Remember to always be yourself. Unless you suck." - Joss Whedon 
"Kindness is more important than wisdom, and the recognition of this is the beginning of wisdom." - Theodore Isaac Rubin 
"Always pass on what you have learned." - Yoda 
"The universe is monstrously indifferent to the presence of man." - Werner Herzog 
"You knock down doors! YOU KICK DOWN WALLS! And ANYBODY, who tells you can't... you take your fears, your insecurities, your worries, roll 'em all up into a ball, TURN THOSE SONS OF BITCHES SIDEWAYS, AND STICK 'EM STRAIGHT UP THEIR CANDY ASSES!" - The Rock 
"I'm not saying I'm gonna change the world, but I guarantee that I will spark the brain that will change the world."  - Tupac Shakur 
"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration." - Nikola Tesla 
"If you always put limit on everything you do, physical or anything else. It will spread into your work and into your life. There are no limits. There are only plateaus, and you must not stay there, you must go beyond them." - Bruce lee 
"We are not human beings having a spiritual experience. We are spiritual beings having a human experience." - Pierre Teilhard de Chardin 
"You can't have everything. Where would you put it?" - Stephen Wright 
"A mind is like a parachute.  It doesn't work if it isn't open" - Frank Zappa 
"Nothing haunts us like the things we don't say." - Mitch Albom 
"Learn how to see.  Realize that everything connects to everything else" - Leonardo da Vinci 
"When you hold on to your history, you do it at the expense of your destiny" - Bishop T.D. Jakes 
"Maybe it's not about the happy ending, maybe it's about the story." 
"A person who truly loves you is someone who sees the pain in your eyes, while everyone else believes in the smile on your face." 
"Falling down is how we grow. Staying down is how we die." - Brian Vaszily 
"If "Plan A" didn't work, the alphabet has 25 more letters!  Stay cool."
"The best way to predict the future is to create it." - Dr. Forrest C. Shaklee 
"A man is but the product of his thoughts.  What he thinks, he becomes." - Mahatma Gandhi 
"We must all face the choice between what is right and what is easy." - Albus Dumbledore 
"Albeit the jealous temper of mankind, ever more disposed to censure than to praise the work of others, has constantly made the pursuit of new methods and systems no less perilous than the search after unknown lands and seas;" - Niccolo  Machiavelli. 
"Nothing is more precious for our people than peace, but it is not something that can be achieved if we simply crave and beg for it." - Kim Jong-Un 
"Work sets you free"
"You don't have a soul. You are a soul. You have a body." - C.S. Lewis 
"Can I trust you? Uh huh then I love you. If not, straight up and down fuck you" - shyheim 
"Just as a candle cannot burn without fire, men cannot live without a spiritual life." - Buddha
"To live is the rarest thing in the world. Most people exist, that is all." - Oscar Wilde 
"The only true wisdom is in knowing you know nothing." --Socrates 
"The beginning is the most important part of the work." - Plato 
"The greater danger for most of us lies not in setting our aim too high and falling short; but in setting our aim too low, and achieving our mark." - Michelangelo 
"Everything that is possible demands to exist." - Gottfried Wilhelm Leibniz 
"People need loving the most when they deserve it the least." - John Harrigan 
"Reality leaves a lot to the imagination." - John Lennon 
"Life is what happens to you while you're busy making other plans." - John Lennon 
"Absence of evidence is not evidence of absence." - Carl Sagan 
"Imagination will often carry us to worlds that never were. But without it we go nowhere." - Carl Sagan 
"Magic is real" - Kav718
"My only regret is that I have but one life to give for my chatroom." - SudokuVegetable
"Has anyone really been far as decided to use even go want to do look more like? You've got to be kidding me. I've been further even more decided to use even go need to do look more as anyone can. Can you really be far even as decided half as much to use go wish for that?" - Anon
"Beauty is truth, truth beauty, - that is all ye know on earth, and all ye need to know." - John Keats
"Let the beauty of what you love be what you do." - Rumi
"Remember all ye that existence is pure joy; that all the sorrows are but as shadows; they pass & are done; but there is that which remains." - Hadit
"Every tree and plant in the meadow seemed to be dancing, those which average eyes would see as fixed and still." - Rumi
'''

BANE_QUOTES = '''It would be extremely painful. 
I AM the League of Shadows, and I'm here to fulfill Ra's al Ghul's destiny! 
You fight like a younger man, with nothing held back. Admirable but mistaken. 
Oh, you think darkness is your ally. But you merely adopted the dark; I was born in it, moulded by it. I didn't see the light until I was already a man, by then it was nothing to me but BLINDING! 
The shadows betray you, because they belong to me! 
I will show you where I have made my home while preparing to bring justice. Then I will break you. 
Ah, yes... I was wondering what would break first... Your spirit, or your body? 
'''

JOKES = '''Never summon Anything you can't banish.
Never put asafoetida on the rocks in the sweat lodge.
Do not attempt to walk more than 10 paces while wearing all of your ritual jewelry, dream bags and crystals at the same time.
When proposing to initiate someone, do not mention the Great Rite, leer, and say, "Hey, your trad or mine?"
Never laugh at someone who is skyclad. They can see you, too.
Never, *ever* set the Witch on fire.
Looking at nifty pictures is not a valid path to mastering the ancient grimoires. Please read thoroughly and carefully from beginning to end so that your madness and gibberings will at least make some sense.
A good grasp of ritual and ritual techniques are essential! In the event of a random impaling, or other accidental death amongst the participants, (see next rule) a quick thinker can improvise to ensure successful completion of the Rite. Make them another sacrifice, Demons really love those those.
Watch where you wave the sharp pointy items.
Avoid walking through disembodied spirits.
Carry an all-purpose translator's dictionary in case the ritual leader begins talking in some strange and unknown language.
Avoid joining your life force to anything with glowing red eyes.
If asked to sign a contract or pact and you are experiencing doubts or reservations, sign your neighbor's name. Malevolent entities rarely ask for photo ID.
Blood IS thicker than water. Soak ritual garments an extra 30-45 minutes.
While drunken waving may be mistaken for ecstatic dancing, slurring the names of Deities is generally considered bad form.
If the ritual leader should ask for a volunteer, resist the urge to raise your hand! While it is true that volunteering will most likely gain you stature and prestige amongst the group, thereby allowing you to advance quickly through the ranks, it is equally likely to get you strapped to a table and eaten alive by a drooling demonic horde.
If you see an onion ring-answer it!
Psychiatrists stay on your mind.
Vitamin C deficiency is apauling.
Astronauts get missile-toe.
Neutrinos have bad breadth.
Zen Druids practice Transcendental Vegetation.
A clear conscience is usually the sign of a bad memory.
'''

NECRONOMICON = '''This is the testimony of all that I have seen, and all that I have learned, in those years that I have possessed the Three Seals of MASSHU. I have seen One Thousand and-One moons, and surely this is enough for the span of a mans life, though it is said the Prophets lived much longer. I am weak, and ill, and bear great tired- ness and exhaustion, and a sigh hangs in my breast like a dark lantern, I am old.
The wolves carry their name in their midnight speeches, and that quiet, subtle Voice is summoning me from afar. And a voice much closer will shout into my ear with unholy impatience. The weight of my soul will decide its final resting place. Before the time, I must put down here all that I can concerning the horrors that stalk Without, and which lie in wait at the door of every man, for this is the ancient arcana that has been handed down of old, but which has been forgotten by all but a few men, the worshippers of the Ancient Ones (may their names be blotted out!)
And if I do not finish this task, take what is here and discover the rest, for time is short and mankind does not know or understand the evil that awaits it, from every side, from every open Gate, from every broken barrier, from every mindless acolyte at the alters of madness.
For this is the Book of the Dead, the Book of the Black Earth, that I have writ down at the peril of my life, exactly as I received it, on the planes of IGIGI, the cruel celestial spirits from beyond the Wanderers of the Wastes.
Let all who read this book be warned thereby that the habitation of men are seen and surveyed by that Ancient Race of gods and demons from a time before time, and that they seek revenge for that forgotten battle that took place somewhere in the Cosmos and rent the Worlds in the days before the creation of Man, when the Elder Gods walked the Spaces, the race of MARDUK, as he is known to the Chaldeans, and of ENKI our master, the Lord of Magicians.
Know, then, that I have trod all the Zones of the Gods, and also the places of Azonei, and have descended into the foul places of Death and Eternal Thirst, which may be reached through the Gate of GANZIR, which was built in UR in the days before Babylonian was.
Know, too, that I have spoken with all manner of spirit and daemon, whose names are no longer known in the societies of Man, or were never known. And the seals of these are writ herein ; yet others I must take with me when I leave you. ANU have mercy on my soul!
I have seen the Unknown Lands, that no map has ever charted. I have lived in the deserts and the wastelands, and spoken with demons and the souls of slaughtered men, and of women who have died in childbirth, victims of the she-fiend LAMMASHTA.
I have traveled beneath the Seas, in search of the Palace of Our Master, and found the stone monuments of vanquished civilizations, and de-ciphered the writings of some of these; while still others remain mysteries to any man who lives. And these civilizations were destroyed because of the knowledge contained in this book.
I have traveled among the stars, and trembled before the gods. I have at last found the formula by which I passed the gate of ARZIR, and passed into the forbidden realms of the foul IGIGI.
I have raised demons, and the dead.
I have summoned the ghosts of my ancestors to real and visible appearance on the tops of temples built to reach the stars, and built to touch the nethermost cavities of HADES. I have wrestled with the Black Magician, AZAG-THOTH, in vain, and fled to the Earth by calling upon INANNA and her brother MARDUK, Lord of the double-headed AXE.
I have raised armies against the Lands of the East, by summoning the hordes of fiends I have made subject unto me, and so doing found NGAA, the god of the heathens, who breathes flame and roars like a thousand thunders.
I have found fear.
I have found the Gate that leads to the Outside, by which the Ancient Ones, who ever seek the entrance to our world, keep eternal watch. I have smelled the vapors of that Ancient One, Queen of the Outside, whose name is writ in the MAGAN text, the testament of some dead civilization whose priests, seeking power, swing open the dread, evil Gate for an hour past the time and were consumed.
I came to possess this knowledge through circumstances quite peculiar, while still the unlettered son of a shepherd in what is called Mesopotamia by the Greeks.
When I was only a youth, traveling alone in the mountains to the East, called MASSHU by the people who live there, I came upon a grey rock carved with three strange symbols. It stood as high as a man, and as wide around as a bull. It was firmly in the ground, and I could not move it. Thinking no more of the carvings, save that they might be the work of a king to mark some Ancient victory over an enemy, I built a fire at its foot to protect me from the from the wolves that wander in that regions and went to sleep, for it was night and I was far from my village, being Bet Durrabia.
Being about three hours from dawn, in the nineteenth of Shabatu, I was awakened by the howl of a dog, or perhaps a wolf, uncommonly loud and close at hand. The fire had died to its embers, and these red, glowing coals cast a faint, dancing shadow across the stone monument with the three carvings. I began to make haste to build another fire when, at once, the grey rock began to rise slowly into the air, as if it were a dove. I could not move or speak for the fear that seized upon my spine and wrapped cold fingers around my skull. The Dik of Azug-bel-ya was no stranger seemed to melt into my hands!
Presently, I heard a voice, softly, some distance away and a more practical fear, that the possibility of robbers, took hold of me and I rolled behind weeds, trembling. Another voice joined the first, and soon several men in black robes of thieves came together over the place where I was, surrounding the floating rock, of which they did not exhibit in the least fright.
I could see clearly now that the three carvings on the stone monument were glowing, a flame red color, as through the rock were on fire. The figures were murmuring together in prayer or invocation, of which only a few words could be heard, and these in some unknown tongue; though, ANU have mercy on my soul!, these rituals are not unknown to me any longer.
The figures, whose faces I could not see or recognize, began to make wild passes in the air with knives that glinted cold and sharp in the mountain night.
From beneath the floating rock, out of the very ground where it had sat, came rising the tail of a serpent. This serpent was surely larger than any I had ever seen. The thinnest section thereof was fully that of the arms of two men, and as it rose from the earth it was followed by another, although the end of the first was not seen as it seemed to reach down into the very Pit itself. These were followed by still more, and the ground began to tremble under the pressure of so many of these enormous arms. The chanting of the priests, for I knew them now to be some the servants of some hidden Power, became much louder and nearly hysterical.
IA! IA! ZI AZAG!
IA!IA! ZI AZKAK!
IA! IA! KUTULU ZI KUR!
IA!
The ground where I was hiding became wet with some substance, being slightly downhill from the scene I was witnessing. I touched the wetness and found it to be blood. In horror I screamed and gave my presence away to the priests. They turned toward me, and I saw with loathing that they had cut their chests with the daggers they had used to raise the stone, for some mystical purpose I could not then divine; although I now know that blood is the very food of these spirits, which is why that field after the battles of war glows with an unnatural light, the manifestation of the spirits feeding thereon.
May ANU protect us all!
My scream had the effect of casting their ritual into chaos and disorder. I raced through the mountain path by which I had come, and the priests came running after me, although some seemed to stay behind, perhaps to finish the Rites. However, as I ran wildly down the slopes in the cold night, my heart gave rise in my chest and my head growing hot, the sound of splitting rocks and thunder came from behind me and shook the very ground I ran on. In fright and haste I fell to the earth.
Rising, I turned to face whatever attacker had come nearest me, though I was unarmed. To my surprise, what I saw was no priest of ancient horror, no necromancer of that forbidden Art, but black robes fallen upon the grass and weeds, with no seeming presence of life or bodies beneath them.
I walked cautiously to the first and, picking up a long twig, lifted the robe from the tangle of weeds and thorns. All that remained of the priest was a pool of slime, like green oil, and the smell of a body lain long in the sun to rot. Such a stench nearly overpowered me, but I was resolute to find the others, to see if the same fortune had also befallen them.
Walking back up the slope that I had so fearfully run down only moments ago, I came across yet another of the black priests, in identical condition to the first. I kept walking, passing more of the robes as I went, not venturing to overturn them any longer. Then, I finally came upon the grey stone monument that had risen unnaturally into the air at the command of the priests. It was now upon the ground once more, but the carvings still glowed with supernatural light. The serpents, or what I had then thought of as serpents, had disappeared. But in the dead embers of the fire, now cold and black, was a shining metal plate.
I picked it up and saw that it was also carved, as the stone, but very intricately, after a fashion I could not understand. It did not bear the same markings as the stone, but I had the feeling I could almost read the characters, but could not, as though I once knew the tongue but had since long forgotten. Mt head began to ache as though a devil was pounding my skull, when a shaft of moonlight hit the metal amulet, for I know now what it was, and a voice entered my head and told me the secrets of the scene I had witnessed in one word: KUTULU.
In that moment, as though whispered fiercely into my ear, I understood. 
Henceforth, from that fateful night in the mountains of MASSHU, I wandered about the countryside in search of the key to the secret knowledge that had been given me. And it was a painful and lonely journey, during which time I took no wife, called no house or village my home, and dwelt in various countries, often in caves or in the deserts, learning several tongues as a traveler, to bargain with the trades people and learn of the news and customs. But my bargaining was with the Powers that reside in each of these countries. And soon, I came to understand many things of which before I had no knowledge, except perhaps in dreams. The friends of my youth deserted me, and I them. When I was seven years gone from my family, I learned that they had all died of their own hand, for reasons no one was able to tell me; their flocks had later been slain as the victims of some strange epidemic.
I wandered as a beggar, being fed from town to town as the local people saw fit, often being stoned instead of threatened with imprisonment. On occasion, I was able to convince some learned man that I was a sincere scholar, and was thereby permitted to read the Ancient Records in which the details of necromancy, sorcery, magick and alchemy are given. I learned of the spells that cause men illness, the plague, blindness, insanity and even death. I learned the various classes of demons and evil gods that exist, and of the old legends concerning the Ancient Ones.
I was thus able to arm myself against the dread Maskim, who lie in wait about the boundaries of the world, ready to trap the unwary and devour the sacrifices set out at night and in deserted places; against the she-devil LAMMASHTA, who is called Sword that Splits the Skull, the sight of whom causes horror and dismay, and (some say) death of a most uncommon nature.
In time I learned of the names and properties of all the demons, devils, fiends and monsters listed herein, in this Book of the Black Earth. I learned of the powers in the astral Gods, and how to summon their aid in times of need. I learned, too, of the frightful beings who dwell beyond the astral spirits, who guard the entrance to the Temple of the Lost, of the Ancient Days the Ancient of the Ancient Ones, whose Name I cannot write here.
In my solitary ceremonies in the hills, worshipping with fire and sword, with water and dagger, and with the assistance of strange grass that grows wild in certain parts of the MASSHU, and with which I had unwittingly built my fire before the rock, that grass that gives the mind great power to travel tremendous distances into the heavens, as also into the hells, I received the formulae for the amulets and talismans which follow, which provide the Priest with safe passage among the spheres wherein he may travel in search of the Wisdom.
But now, after One Thousand-and-One moons of the journey, the Maskim nip at my heels, the Rabishu pull at my hair, Lammashta opens her dread jaws, AZAG-THOTH gloats blindly at his throne, KUTULU raises his head and stares up through the Veils of sunkun Varloorni, up through the Abyss, and fixes his stare upon me; wherefore I must with haste write this Book lest my end come sooner than I had prepared. For indeed, it appears as though I have failed in some regard as to the order of the rites, or to the formulae, or to the sacrifices, for now it appears as if the entire host of ERESSKIGAL lies waiting, dreaming, drooling for my departure.
I pray the gods that I am saved (which he is not, for "gods" cannot save ones soul, only GOD) and not perish as did the Priest, ABDUL BEN-MARTU, in Jerusalem (the gods remember and have mercy upon him!). My fate is no longer writ in the stars, for I have broken the Chaldean Covenant by seeking power over the Zonei. I have set foot on the moon, and the moon no longer has power over me. The lines of my life have been obliterated by my wanderings in the Waste, over the letters writ in the heavens by the gods. And even now I can hear the wolves howling in the mountains as they did that fateful night, and they are calling my name, and the names of the Others. I fear for my flesh, but I fear for my spirit more.
Remember, always, in every empty moment, to call upon the gods not to forget thee, for they are forgetful and very far away. Light thy fires high in the hills, and on the tops of temples and pyramids, that they may see and remember.
Remember, always, to copy each of the formulae as I have put it down and not to change it by one line or dot, not so much as hair's breadth, lest it be rendered valueless, or worse: a broken line provides means of entrance for those Outside, for a broken star is the Gate of GANZIR, the Gate of Death, the Gate of the Shadows and the Shells. Recite the incantations as they are written here, in the manner thus prescribed. Prepare the rituals without erring, and in the proper places and times render the sacrifices.
May the gods ever be merciful unto thee!
May thou escape the jaws of the MASKIM, and vanquish the power to the Ancient Ones!
AND THE GODS GRANT THEE DEATH BEFORE THE ANCIENT ONES RULE THE EARTH ONCE MORE!
KAKAMMU! SELAH!
The Old Ones were, the Old Ones are and the Old Ones shall be. From the dark stars They came ere man was born, unseen and loathsome They descended to primal earth. Beneath the oceans They brooded while ages past, till seas gave up the land, whereupon They swarmed forth in Their multitudes and darkness ruled the Earth.
At the frozen Poles They raised mighty cities, and upon high places the temples of Those whome nature owns not and the Gods have cursed.
And the spawn of the Old Ones covered the Earth, and Their children endureth throughout the ages. Ye shantaks of Leng are the work of Their hands, the Ghasts who dwelleth in Zin's primordial vaults know Them as their Lords.
They have fathered the Na-Hag and the Gaunts that ride the Night; Great Cthulhu is Their brother, the shaggoths Their slaves. The Dholes do homage unto Them in the nighted vale of Pnoth and Gugs sing Their praises beneath the peaks of ancient Throk.
They have walked amidst the stars and They have walked the Earth. The City of Irem in the great desert has known Them; Leng in the Cold Waste has seen Their passing, the timeless citadel upon the cloud-vieled heights of unknown Kadath beareth Their mark.
Wantonly the Old Ones trod the ways of darkness and Their blasphemies were great upon the Earth; all creation bowed beneath Their might and knew Them for Their wickedness.
And the Elder Lords opened Their eyes and beheld the abominations of Those that ravaged the Earth. In Their wrath They set their hand against the Old Ones, staying Them in the midst of Their iniquity and casting Them forth from the Earth to the Void beyond the planes where chaos reigns and form abideth not. And the Elder Lords set Their seal upon the Gateway and the power of the Old Ones prevailest not against its might.
Loathsome Cthulhu rose then from the deeps and raged with exceeding great fury against the Earth Guardians. And They bound his venomous claws with potent spells and sealed him up within the City of R'lyeh wherein beneath the waves he shall sleep death's dream until the end of the Aeon.
Beyond the Gate dwell now the Old Ones; not in the spaces known unto men but in the angles betwixt them. Outside Earth's plane They linger and ever awaite the time of Their return; for the Earth has known Them and shall know Them in time yet to come.
And the Old Ones hold foul and formless Azathoth for Their Master abd Abide with Him in the black cavern at the centre of all infinity, where he gnaws ravenously in ultimate chaos amid the mad beating of hidden drums, the tuneless piping of hideous flutes and the ceaseless bellowing of blind idiot gods that shamble and gesture aimlessly for ever.
The soul of Azathoth dwelleth in Yog-sothoth and He shall beckon unto the Old Ones when the stars mark the time of Their coming; for Yog-sothoth is the Gate through which Those of the Void will re-enter. Yog-sothoth knowest the mazes of of time, for all time is one unto Him. He knowest where the Old Ones came forth in time along long past and where They shall come forth again when the cycle returneth.
After day cometh night; man's day shall pass, and They shall rule where They once ruled. As foulness you shall know them and Their accursedness shall stain the Earth.
Whenever thou would'st call forth Those from Outside, thou must mark well the seasons and times in which the spheres do intersect and the influences flow from the Void
Thou must observe the cycle of the Moon, the movements of the planets, the Sun's course through the Zodiac and the rising of the constellations.
Ye Ultimate Rites shall be performed only in the seasons proper to them, these be: at Candlemas (on the second day of the second month), at Beltane (on the Eve of May), at Lammas (on the first day of the eighth month), at Roodmas (on the fourteenth day of the ninth month), and at Hallowmas (on November Eve).
Call out to dread Azathoth when the Sun is in the sign of the Ram, the Lion, or the Archer; the Moon decreasing and Mars and Saturn conjoin.
Mighty Yog-sothoth shall rise to ye incantations when Sol has entered the fiery house of Leo and the hour of Lammas be upon ye.
Evoke ye terrible Hastur on Candlemas Night, when Sol is in Aquarius and Mercury in trine.
Supplicate Great Cthulhu only at Hallowmas Eve when the Sun abides within the House of the Scorpion and Orion riseth. When All Hallows falls within the cycle of the new Moon the power shall be the strongest.
Conjure Shub-Niggurath when the Beltane fires glow upon the hills and the Sun is in the Second House, repeating the Rites of Roodmas when ye Black One appeareth.
Who seeketh Northwards beyond the twilight land of Inquanok shall find amidst the frozen waste the dark and mighty plateau of thrice-forbidden Leng.
Know ye time-shunned Leng by the ever-burning evil-fires and ye foul screeching of the scaly Shantak birds which ride the upper air; by the howling of ye Na-hag who brood in nighted caverns and haunt men's dreams with strange madness, and by the grey stone temple beneath the Night Gaunts lair, wherein is he who wears the Yellow Mask and dwelleth all alone.
But beware O Man, beware, of Those who tread in Darkness the ramparts of Kadath, for he that beholds Their mitred-heads shall know the claws of doom.
Of Kadath Ye Unknown
What man knoweth Kadath?
For who shall know of that which ever abides in strange-time, twix yesterday, today and the morrow.
Unknown amidst ye Cold Waste lieth the mountain of Kadath where upon the hidden summit an Onyx Castle stands. dark clouds shroud the mighty peak that gleams 'neath ancient stars where silent brood the titan towers and rear forbidden walls.
Curse-runes guard the nighted gate carved by forgotten hands, and woe to he that dare pass within those dreadful doors.
Earth's Gods revel where Others once walked in mystic timeless halls, which some have glimpst in sleeps dim vault through strange and sightless eyes.
'''

SONGS = '''Twinkle, twinkle, little star, how I wonder what you are! Up above the world so high, Like a diamond in the sky~
I don't eat~ I don't sleep~ I do nothing but think of you~
You keep me under your spell~ You keep me under your spell~ You keep me under your spell~'''