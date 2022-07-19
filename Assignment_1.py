#!/usr/bin/env python
# coding: utf-8

# In[ ]:


q1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.

Ans :1)   *      = operator
     2)  'hello' = string vlaue
     3)  -87.8   = value
     4)   -      = operator
     5)   /      = operator
     6)   +      = operator
     7)   6      = integer value


get_ipython().set_next_input('Q2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans :- string is a datatype while variables are container for storing data values. 
    for ex :- s = 'prem' , here "s" is a variable and 'prem' is string.


Q3. Describe three different data types.

Ans :- text type = str
       Numeric Type = int , float , complex
       Boolean Type = Bool


get_ipython().set_next_input('Q4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Ans :- An expression is a combination of operator, variables, value. Expressions need to be evaluated . All expressions 
evaluate to a single value.


get_ipython().set_next_input('Q5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Ans :- Expression is made up of values, containers, and mathematical operators (operands) and the statement is just 
like a command that a python interpreter executes like print and assignment statements.


# In[ ]:


get_ipython().set_next_input('Q6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[1]:


bacon = 22


# In[2]:


bacon+1


# In[ ]:


it will gives 23


# In[ ]:


get_ipython().set_next_input('Q7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3


# In[3]:


'spam' + 'spamspam' 


# In[4]:


'spam' * 3


# In[ ]:


both are giving the same value


# In[ ]:


get_ipython().set_next_input('Q8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Ans :- because in python it is a rule that, A variable can not start with an integer, therefore 100 can not be the variable name.
    
    
get_ipython().set_next_input('Q9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')

Ans :- int(), float(), str()
    
    
get_ipython().set_next_input('Q10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'

Ans :- because 99 ia an integer and we can concatenated string to other string.
       so, the correct wat is 'i have eaten' + str(99) + 'burritos'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




