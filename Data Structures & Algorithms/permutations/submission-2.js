class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        let res = [] 

        function backtrack(path,index) {
            if (path.length == nums.length) {
                res.push([...path]) 
                return 
            } 

            for (let i = 0 ; i < nums.length ; i++) {
                if (path.includes(nums[i])){
                    continue
                }
                path.push(nums[i])
                backtrack(path,i+1) 
                path.pop()
             }
        }
        backtrack([],0) 
        return res
    }
}
