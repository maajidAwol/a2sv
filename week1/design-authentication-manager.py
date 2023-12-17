class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.users = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.users[tokenId] = currentTime + self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.users.get(tokenId,-1) !=-1 and self.users[tokenId] > currentTime:
            self.users[tokenId] = currentTime + self.time
    def countUnexpiredTokens(self, currentTime: int) -> int:      
        unexpired = [user for user in self.users.values() if user > currentTime]
        return len(unexpired)
# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)