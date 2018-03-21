/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let sArr = s.split('')
    let arr = []
    let map = {')': '(', ']': '[','}': '{'}
    
    if(sArr.length % 2 !== 0){
        return false
    }
    
    for(let i = 0; i < sArr.length; i++){
        if(sArr[i] === '{' || sArr[i] === '[' || sArr[i] === '('){
            arr.push(sArr[i])
        }
        else if(sArr[i] === '}' && arr[arr.length-1] === '{'){
            arr.pop()        
        }  
        else if(sArr[i] === ']' && arr[arr.length-1] === '['){
            arr.pop()        
        } 
        else if(sArr[i] === ')' && arr[arr.length-1] === '('){
            arr.pop()        
        } 
        else if(map[sArr[i]] !== arr[arr.length-1]){
            return false            
        }
    }
    
    return arr.length === 0
};
