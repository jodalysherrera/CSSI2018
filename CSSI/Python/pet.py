dog ={
    'name':'doggy mcdogface',
    'breed':'terrier',
    'age' : 2,
    'hungry': True,
    'sleepy': False,
}

class Dog(object): #always define class upper
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.needs_a_walk= True
        self.is_sleepy=False

    def feed(self):
        self.is_hungry=False
        print('nomnomnomnomnomnom')

    def walk(self):
        if self.needs_a_walk==True and not self.is_sleepy:
            self.needs_a_walk= False
            self.is_sleepy = True
            print('walkawalkawalkawalka')

    def sleep(self):
        if self.is_sleepy == True:
            self.is_sleepy = False
            self.is_hungry==True
            print('yawn ZzZzZz')

    def play(self, other_dog):
        print('%s is playing with %s' % (self.name, other_dog.name))

    def __str__(self): #helps learn more specific about this object
        return '%s who is %s' % (self.name,self.age)
        # print(type(dog1))
        #WHEN PRINTING WILL USE THIS AS A STRING RATHER THAN WHOLE THING

dog1=Dog('doggy mcdogface',2)
dog2=Dog('buster',1)

dog1.name='ruff'

print (dog1.name) #. is associated with objects, and can acess properties
print('%s is %s years old' % (dog1.name,dog1.age))
#print(type(dog1))

dog1.feed()
dog1.walk()
dog1.walk()
dog1.feed()
dog1.sleep()
dog1.walk()
dog1.sleep()
dog1.feed()
dog1.walk()

print dog1.is_hungry


print(dog1)
print(dog2)
dog1.play(dog2)
dog2.play(dog1)
