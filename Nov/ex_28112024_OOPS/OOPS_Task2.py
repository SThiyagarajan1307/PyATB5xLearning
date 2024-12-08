# Create a Class Name API - RestfulBooker
#
# name, list_of_api , links {}
#
# print_apis, print_set()

class API:
    Name = None
    list_of_apis = []
    links = {}

    def __init__(self, name, list_api, links):
        self.Name = name
        self.list_of_apis = list_api
        self.links = links

    def print_apis(self):
        print(f"Name {self.Name}, list of APIs{self.list_of_apis}")
        for i in self.list_of_apis:
            print(i)

    def print_set(self):
        print(f"Name {self.Name}, list of APIs{self.links}")
        for i in self.links:
            print(i)


api = API("SOAP", ["Rest Assured", "SOAP", "TCP"], {"www.hello.com", "www.restassure.com"})
api.print_apis()
api.print_set()
