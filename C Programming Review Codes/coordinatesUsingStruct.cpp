#include <iostream>
#include <cmath>
using namespace std;

// Define the Point structure here
struct point{
	float x;
    float y;
};

// Define the calculateDistance function here
float calculateDistance(point p1,point p2){
	
    float distance = sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
    return distance;
}

int main() {
    // Create two Point objects and input their coordinates from the user
    point p1;
    point p2;
    
    cout << "For point 1, input the X: " << endl;
    cin >> p1.x;
    cout << "Input the point Y: " << endl;
    cin >> p1.y;
    
    cout << "For point 2, input the X: " << endl ;
    cin >> p2.x;
    cout << "Input the point Y: " << endl;
    cin >> p2.y;
    
    // Calculate the distance between the two points using calculateDistance
	float answer = calculateDistance(p1, p2);
    
    // Display the calculated distance
    cout << "" << answer;

    return 0;
}
