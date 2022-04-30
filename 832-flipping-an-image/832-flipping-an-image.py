class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for irow in range(len(image)):
            image[irow] = image[irow][::-1]
            for i in range(len(image[irow])):
                if image[irow][i] == 0:
                    image[irow][i] = 1
                else:
                    image[irow][i] = 0
        return image
