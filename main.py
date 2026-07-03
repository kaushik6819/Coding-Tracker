import json


class Question:
    def __init__(self,question_id,name,platform,link,practiced=0,last_practiced="",topic="General"):
        self.question_id = question_id
        self.name = name
        self.platform = platform
        self.link = link
        self.practiced = practiced
        self.last_practiced = last_practiced
        self.topic = topic

    def to_dict(self):
        return{
            "id":self.question_id,
            "name":self.name,
            "platform":self.platform,
            "link":self.link,
            "practiced":self.practiced,
            "last_practiced" : self.last_practiced,
            "topic" : self.topic
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            question_id = data["id"],
            name = data["name"],
            platform = data["platform"],
            link = data["link"],
            practiced =data["practiced"],
            last_practiced= data["last_practiced"],
            topic = data["topic"]

        )    
    
question = Question(question_id=1, name="Two Sum", platform="LeetCode",
                     link="https://leetcode.com/problems/two-sum/", topic="Array")

class QuestionStore:
    def __init__(self,filename = "coding_tracker.json"):
        self.filename = filename
        self.questions =[]
        self.load()

    def load(self):
        with open(self.filename,"r") as file:
            raw_data = json.load(file)
        
        self.questions =[]
        for item in raw_data:
            question =Question.from_dict(item)
            self.questions.append(question)


data = question.to_dict()
print(data)

rebuilt = Question.from_dict(data)
print(rebuilt.name, rebuilt.platform, rebuilt.topic)