import abc
import os
import sys
# Author Robin Viera 
# Data 07/05/2021
# Description: This class scan directories recursively and creates a directory tree as a result
# in the form of a list of strings



class Interface_MetaDir(abc.ABC):

    @classmethod
    def __subclasshook__(cls,subclass):
        
        return (hasattr(subclass,"ExploreDirectories") and 
        callable(subclass.Set_Path) and
        hasattr(subclass,"Get_Root_Folder_Path") and
        callable(subclass.Get_Path))

    @abc.abstractmethod
    def ExploreDirectories(self,path:str)->bool:
        "set path root for path explorer, returns tow lists elements"
        raise NotImplemented

    @abc.abstractmethod
    def Get_Root_Folder_Path(self)->str:
        "Return the full path to the root"
        raise NotImplemented



class TreeExplorer(Interface_MetaDir):



    def __init__(self):

        self.Files_Registry={}
        self.Dir_Registry={}
        self.Files_List=[]
        self.Dir_List=[]
        self.Dir_Map=[]
        self.w_slash=""
        self.path=""
        self.new_path=""



    def ExploreDirectories(self,path:str="",mode:str="absolute")->list:
        
        self.Files_Registry={}
        self.Dir_Registry={}
        self.Files_List=[]
        self.Dir_List=[]
        self.Dir_Map=[]

        if sys.platform == "linux":
            self.w_slash="/"
        else:
            self.w_slash="\\"

        current_dir=""
        if path=="" and mode=="":  
            current_dir=os.getcwd()
        elif mode=="absolute" and  path !="":
            current_dir=path
        elif mode=="relative" and path !="":
            current_dir=os.getcwd()
            current_dir=current_dir+self.w_slash+path

        if os.path.isdir(current_dir):
            self.path=current_dir
            self.__Create_Directory_Tree()
        else:
            return False
            


 
    def Get_Root_Folder_Path(self)->str:
        
        if(self.path != ""):
            return self.path
        else:
            print(" Path not defined ")
            return False




    def __Create_Directory_Tree(self):
        
        self.__Print_ROOT(self.path)
        self.__Explore_Directories(self.path)
      



    def __Explore_Directories(self,root:str):

        Current_Dir_Entries=os.scandir(root)

        for entry in Current_Dir_Entries:

            self.new_path=root+self.w_slash+entry.name
            length=self.__Check_Element_Length(self.new_path)
            name=str(entry.name)
            path=str(entry.path)

            if entry.is_dir():
                self.Dir_Registry.update({name:path})
                self.Dir_List.append(path)

                self.__Print_DIR(name,length)
                self.__Explore_Directories(self.new_path)
            else:
                self.Files_Registry.update({name:path})
                self.Files_List.append(path)
                
                self.__Print_File(name,length)

                
                    

    def __Check_Element_Length(self,characters:str):
        
        branch_length=0
        for character in characters:
            if character == self.w_slash:
                branch_length+=1

        return branch_length



    def __Print_ROOT(self,path:str):

        start=path.rfind(self.w_slash)
        end=len(path)
        i=0
        string=""
        for i in range(start,end):    
            string=string+path[i]
        string="/ROOT/ - "+string
        self.__Print_DIR(string,0)




    def __Print_DIR(self,entry:str,length:int):

        print(self.__Space())
        string=self.__Add_Indentation_Dir(length)
        string=string+" "+entry
        self.Dir_Map.append(string)
        print(string)




    def __Print_File(self,entry:str,length:int):
   
        string=self.__Add_Identation_File(length)
        string=string+" "+entry
        self.Dir_Map.append(string)
        print(string)




    def __Add_Identation_File(self,identation:int)->str:

        base_string=""

        for space in range(identation):
            base_string=base_string+" "
        base_string=base_string+"|"

        for space in range(identation):
            base_string=base_string+"-"
        base_string="|"+base_string

        return base_string



    def __Space(self)->str:

        return "|"



    def __Add_Indentation_Dir(self,identation:int)->str:
        
        base_string=""

        for space in range(identation):
            base_string=base_string+"-"
        base_string="|"+base_string

        return base_string


