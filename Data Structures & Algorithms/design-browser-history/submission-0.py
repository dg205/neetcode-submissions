class ListNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage) 
        

    def visit(self, url: str) -> None:
        newnode = ListNode(url)
        self.current.next = newnode
        newnode.prev = self.current
        self.current = newnode

        

    def back(self, steps: int) -> str:
        while self.current.prev and steps != 0:
            self.current = self.current.prev
            steps -= 1
        
        return self.current.url


    def forward(self, steps: int) -> str:
        while self.current.next and steps != 0:
            self.current = self.current.next
            steps -= 1
        
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)