#     after running the python file just press enter it will automatically read my self created agent.csv or
#                                 you can enter your own file
#      Note:the program runs on csv file 
import numpy as np
import pandas as pd

# this is the function for agent selection

def agent_selector(agent_df,mode,issue=None):
    
    # Created a copy of dataframe so the real data is not manipulated
    
    agent_df_copy=agent_df.copy()
    agent_df_copy=agent_df_copy.loc[agent_df_copy.is_available==True]
    
    # Function for advance case so that it works according to issue provided
    
    def issue_select(agent_df_copy,issue=None):
        idx=[]
        final_idxs=[]
        for row in agent_df_copy.roles:
            if issue in row:
                idx.append(agent_df_copy.index[agent_df_copy.roles==row])
        for i in idx:
            for j in i:
                final_idxs.append(j)
        final_idxs=set(final_idxs)
        agent_df_copy=agent_df_copy.loc[final_idxs]
        return agent_df_copy
    agent_df_copy=issue_select(agent_df_copy,issue)
    
    # the desired cases for the function are as follows
    
    if mode == "all available":
        return agent_df_copy
    elif mode == "least busy":
        least=list(agent_df_copy.available_since)
        empty=min(least)
        return agent_df_copy.loc[agent_df_copy.available_since==empty]
    elif mode == "random":
        return agent_df_copy.sample()
    else:
        print("wrong input")
        
#   In the following lines if you press enter agent.csv will be called automatically or 
#      you can enter your own file for testing
        
agent_list=input("Enter your file name or press enter")
if (len(agent_list) < 1): agent_list ='agent.csv'
agent_df=pd.DataFrame(pd.read_csv(agent_list))
mode=input("Please enter the mode\t")
issue=input("Please enter issue(eg. sales or support)\t ")
print("Your agent is :\n",agent_selector(agent_df,mode,issue).to_string(index=False))
