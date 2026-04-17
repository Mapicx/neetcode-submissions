class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(speed, position),key= lambda x:x[1] ,reverse= True)
        sorted_speed, sorted_position = zip(*combined)

        speed = list(sorted_speed)
        position = list(sorted_position)

        if len(position) == 1:
            return 1

        time_stack = []

        for i in range(len(sorted_position)):
            curr_time = (target - position[i]) / speed[i]
            if not time_stack:
                time_stack.append(curr_time)
            else:
                if time_stack[-1] < curr_time:
                    time_stack.append(curr_time)
                else:
                    pass
        
        return len(time_stack)



        