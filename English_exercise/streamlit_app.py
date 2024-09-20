#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

tasks = [
	{'sentence' : '_____ Red Riding Hood',
    'options' : [['Little','Littlest', ' Littler']],
    'answer' : ['Little'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : 'Charles _____',
    'options' : [['Perrault','Lang','DeGaulles']],
    'answer' : ['Perrault'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : 'Once upon a time there _____ in a certain village a little country girl, the _____ creature who was ever seen.',
    'options' : [['living', 'resided', 'lived'],['prettiest', 'loveliest','ugliest']],
    'answer' : ['lived', 'prettiest'],
    'result'  : ['', ''],
    'total'   : 0,
    },
                  
	{'sentence' : 'Her mother was _____ fond of her; and her grandmother doted on her still more.',
    'options' : [['overly', 'excessively', 'extraordinarily']],
    'answer' : ['excessively'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'This good _____ had a Little red riding hood made for her.',
    'options' : [['woman','girl','mother']],
    'answer' : ['woman'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'It _____ the girl so extremely well that everybody _____ her Little Red Riding Hood.',
    'options' : [['suits', 'suited', 'suit'],['call', 'calls','called']],
    'answer' : ['suited', 'called'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : 'One day her mother, having made some _____, said to her, "Go, my _____, and see how your _____ is doing, for I hear she has been very ill.',
    'options' : [['cakes', 'cake'],['dears', 'dear'],['grandmother', 'grandmothers']],
    'answer' : ['cakes', 'dear', 'grandmother'],
    'result'  : ['', '', ''],
    'total'   : 0,
    },

	{'sentence' : '_____',
    'options' : [['Take her a cake, and this little pot of butter.',
                'Go her a cake, and this little pot of butter.',
                'Forced her a cake, and this little pot of butter.']],
    'answer' : ['Take her a cake, and this little pot of butter.'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'Little Red Riding Hood set out _____ to go to her grandmother, who lived in another village.',
    'options' : [['soon', 'quickly', 'immediately']],
    'answer' : ['immediately'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'As she was _____ through the wood, she met with a wolf, who had a very _____ mind to eat her up, but he dared not, because of some woodcutters _____ nearby in the forest.',
    'options' : [['go', 'goes','going'],['greatest', 'great','greater'],['works', 'working', 'wrought']],
    'answer' : ['going', 'great', 'working'],
    'result'  : ['', '', ''],
    'total'   : 0,
    },

	{'sentence' : 'He _____ her where she was _____.',
    'options' : [['ask', 'asks','asked'],['going', 'goes','went']],
    'answer' : ['asked', 'going'],
    'result'  : ['', ''],
    'total'   : 0,
    },
	
	{'sentence' : 'The poor child, who did not know that it was _____ to stay and talk to a wolf, said to him, "I am going to see my grandmother and _____ her a cake and a little pot of butter from my mother."',
    'options' : [['difficult', 'dangerous','potentially'],['carry', 'carrying ','carried']],
    'answer' : ['dangerous', 'carry'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : '"Does she _____ far off?" said the wolf',
    'options' : [['lived', 'lives', 'live']],
    'answer' : ['live'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : '"Oh I say," answered Little Red Riding Hood; "it is beyond that mill you see there, at the _____ house in the village."',
    'options' : [['firstest', 'first', 'firster']],
    'answer' : ['first'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : "'Well,' said the wolf, 'and I'll go and see her too. I'll go this _____ and go you that, and we shall see who will be _____ first.'",
    'options' : [['turn ', 'going','way'],['only', 'there','this']],
    'answer' : ['way', 'there'],
    'result'  : ['', ''],
    'total'   : 0,
    },
	
	{'sentence' : 'The wolf ran as fast as he could, taking the shortest _____, and the little girl took a _____ way, entertaining herself by gathering nuts, running after _____, and gathering bouquets of little flowers.',
    'options' : [['path', 'toward','paths'],['thoroughfare', 'roundabout','intersection'],['butterflies', 'moths', 'insects']],
    'answer' : ['path', 'roundabout', 'butterflies'],
    'result'  : ['', '', ''],
    'total'   : 0,
    },
	
	{'sentence' : "It was not long before the wolf arrived at the old woman's _____.",
    'options' : [['house', 'office', 'room']],
    'answer' : ['house'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'He _____ at the door: tap, tap.',
    'options' : [['knocked', 'knockes', 'knock']],
    'answer' : ['knocked'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : "Who's _____?",
    'options' : [['there', 'they', 'this']],
    'answer' : ['there'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : ' "Your grandchild, Little Red Riding Hood," replied the wolf, _____ her voice; "who has brought you a cake and a little pot of _____ sent you by mother."',
    'options' : [['counterfeit', 'counterfeiting','laundering'],['vanilla', 'cream ','butter']],
    'answer' : ['counterfeiting', 'butter'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : 'The _____ grandmother, who was in bed, because she was somewhat ill, cried out, "Pull the _____, and the latch will go up."',
    'options' : [['good', 'better','sure'],['bobbin', 'rollin','moire']],
    'answer' : ['good', 'bobbin'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : 'The wolf _____ the bobbin, and the door opened, and then he immediately fell upon the good woman and ate her up in a _____, for it been more than three days since he had eaten.',
    'options' : [['pulled', 'pushed','picked'],['thing', 'mind','moment']],
    'answer' : ['pulled', 'moment'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : "He then shut the _____ and got into the grandmother's bed, _____ Little Red Riding Hood, who came some time afterwards and knocked at the door: tap, tap.",
    'options' : [['door', 'window','room'],['anticipating', 'expecting','expect']],
    'answer' : ['door', 'expecting'],
    'result'  : ['', ''],
    'total'   : 0,
    },
	
	{'sentence' : 'Little Red Riding Hood, _____ the big voice of the wolf, was at first afraid; but _____ her grandmother had a cold and was hoarse, answered, "It is your _____ Little Red Riding Hood, who has brought you a cake and a little pot of butter mother sends you."',
    'options' : [['proceedings', 'hearing','hearings'],['believing', 'afraid ','knowing '],['grandchild', 'granddaughter', 'grandchildren']],
    'answer' : ['hearing', 'believing', 'grandchild'],
    'result'  : ['', '', ''],
    'total'   : 0,
    },

	{'sentence' : 'The wolf cried out to her, _____ his voice as much as he could, "Pull the bobbin, and the _____ will go up."',
    'options' : [['weakening', 'softening','hardening'],['latches', 'locking','latch']],
    'answer' : ['softening', 'latch'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : '_____',
    'options' : [['Much Red Riding Hood picked the weft, and the doors held.',
                'Little Red Riding Hood pulled the bobbin, and the door opened.',
                'Big Red Riding Hood knocked the toupee, and the doors reopened.']],
    'answer' : ['Little Red Riding Hood pulled the bobbin, and the door opened.'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'The wolf, _____ her come in, said to her, hiding himself under the _____, "Put the cake and the little pot of butter upon the stool, and come get into bed with me."',
    'options' : [['looking', 'seeing','watching'],['bedclothes', 'bedcovers','nightclothes']],
    'answer' : ['seeing', 'bedclothes'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : '_____',
    'options' : [['Much Red Riding Hood taken off her clothing and just into beds.',
                'Little Red Riding Hood took off her clothes and got into bed.',
                'Ugly Red Riding Hood came off her shoes and got into sleeping.']],
    'answer' : ['Little Red Riding Hood took off her clothes and got into bed.'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : ' She was greatly _____ to see how her grandmother looked in her nightclothes, and said to her, "Grandmother, what big _____ you have!"',
    'options' : [['amazed', 'astonished','astounded'],['weapons', 'arms','guns']],
    'answer' : ['amazed', 'arms'],
    'result'  : ['', ''],
    'total'   : 0,
    },

	{'sentence' : '_____',
    'options' : [['All the better to hug you with, my dear.',
                'All the make to hugged you with, my goodbye.',
                'All the worse to kiss you with, my hello.']],
    'answer' : ['All the better to hug you with, my dear.'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : 'Grandmother, what big _____ you have!',
    'options' : [['neck', 'legs', 'knees']],
    'answer' : ['legs'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'All the better to _____ with, my child.',
    'options' : [['run', 'start', 'go']],
    'answer' : ['run'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : 'Grandmother, what big _____ you have!',
    'options' : [['eyes', 'noses', 'ears']],
    'answer' : ['ears'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : '_____',
    'options' : [['All the better to hear with, my child.',
                'All the even to goodbye you with, my sorry.',
                'All the make to kiss you with, my my.']],
    'answer' : ['All the better to hear with, my child.'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : '_____',
    'options' : [['Grandmother, what huge ears you been!',
                'Grandmother, what losses swollen you had!',
                'Grandmother, what big eyes you have!']],
    'answer' : ['Grandmother, what big eyes you have!'],
    'result'  : [''],
    'total'   : 0,
    },
		
	{'sentence' : 'All the better to see _____, my child.',
    'options' : [['both', 'with', 'over']],
    'answer' : ['with'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : 'Grandmother, what big _____ you have got!',
    'options' : [['tooth', 'bones', 'teeth']],
    'answer' : ['teeth'],
    'result'  : [''],
    'total'   : 0,
    },

	{'sentence' : '_____',
    'options' : [['All the because to consume you up with.',
                'All the good to ate you up with.',
                'All the better to eat you up with.']],
    'answer' : ['All the better to eat you up with.'],
    'result'  : [''],
    'total'   : 0,
    },
	                  
    	{'sentence' : 'And, saying these words, this _____ wolf fell upon Little Red Riding Hood, and ate her all up.',
    'options' : [['wicked', 'evil', 'crazy']],
    'answer' : ['wicked'],
    'result'  : [''],
    'total'   : 0,
    },
	
	{'sentence' : 'Moral: Children, especially _____, well bred young ladies, should never talk to strangers, for if they should do so, they may well provide _____ for a wolf.',
    'options' : [['desirable ', 'attractive','expensive'],['dinner', 'breakfast','lunch']],
    'answer' : ['attractive', 'dinner'],
    'result'  : ['', ''],
    'total'   : 0,
    },
	
	{'sentence' : 'I say "wolf," but there are _____ kinds of wolves.',
    'options' : [['several', 'various', 'different']],
    'answer' : ['various'],
    'result'  : [''],
    'total'   : 0,
    },	
	
	{'sentence' : 'There are also those who are _____, quiet, polite, unassuming, complacent, and sweet, who pursue young women at home and in the _____.',
    'options' : [['beautiful', 'lovely','charming'],['sidewalks', 'streets','downtown']],
    'answer' : ['charming', 'streets'],
    'result'  : ['', ''],
    'total'   : 0,
    },	
	
	{'sentence' : ' And unfortunately, it is these _____ wolves who are the most dangerous ones of all.',
    'options' : [['gentle', 'charming', 'pleasant']],
    'answer' : ['gentle'],
    'result'  : [''],
    'total'   : 0,
    },
	
]

  
st.header('English exercise generator')
st.subheader('Insert text to create an exercise')

st.text_area('nolabel', label_visibility="hidden")

'---'

st.subheader('Choose the correct answer:')

for task in tasks:
    col1, col2 = st.columns(2)
    with col1:
        st.write('')
        st.write(str(task['sentence']))
        
    with col2:
        for i in range(len(task['options'])):
            option = task['options'][i]
            task['result'][i] = st.selectbox('nolabel', 
                                             ['–––'] + option, 
                                             label_visibility="hidden")
            if task['result'][i] == '–––':
                pass
            elif task['result'][i] == task['answer'][i]:
                st.success('', icon="✅")
            else:
                st.error('', icon="😟")
    task['total'] = task['result'] == task['answer']    
    '---'        
                 
total_sum = sum(task['total'] for task in tasks)

if total_sum == len(tasks):
    st.success('Успех!')
    st.balloons()
    



