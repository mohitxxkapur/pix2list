the goal of this is to instantly go from voxel to partslist to save myself some time

__done__
- sorting
- counting occurences of colour
  
__to do:__
- find neigbors

finding the neighbors will be very interesting - at first I thought I would just be able to look at the next element in the list, but that is incorrect.
We will need to go through the list entirely to find the piece next to it using the x y z values.
Assuming I have the theory correct, the algorithm will look something lik=e this:
_if it exists in the part list that there is a piece with the same y and z values AND the x value is exactly one more or one less than our current x value, then add one to the count. Repeat for Y and Z. Add the total count to the tuple and move onto the next part in the list_

- convert to correct piece


https://www.slynyrd.com/blog/2019/5/21/pixelblog-17-human-anatomy
