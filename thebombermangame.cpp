int rows, columns;

int main() {
    
    int seconds;
    
    cin >> rows >> columns >> seconds;
    
    vector<vector<char>> arr(rows, vector<char>(columns));
    vector<vector<char>> arrFull(rows, vector<char>(columns, 'O'));
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            cin >> arr[i][j];
        }
    }
    
    if(seconds == 1){
        printVector(arr);
    } else {
        switch (seconds % 4){
            case 1:
                printVector(getExploded(getExploded(arr)));
                break;
            case 3:
                printVector(getExploded(arr));
                break;
            default:
                printVector(arrFull);
        }
    }
    
    return 0;
}

//see if a point is out of bounds
bool outOfBounds(int xPos, int yPos){
    bool thing = (xPos >= 0 && xPos < columns && yPos >= 0 && yPos < rows);
    return !thing;
}

//print a given vector
void printVector(const vector<vector<char>> arr){
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            cout << arr[i][j];
        }
        cout << endl;
    }
}

//explode the bombs in a given grid
vector<vector<char>> getExploded(const vector<vector<char>>input){
   
    vector<vector<char>> arrAlt(rows, vector<char>(columns,'O'));

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            if(input[i][j] == 'O'){
                arrAlt[i][j] = '.';
                
                if(!outOfBounds(j-1, i)){
                    arrAlt[i][j-1] = '.';
                }
                
                if(!outOfBounds(j+1, i)){
                    arrAlt[i][j+1] = '.';
                }
                
                if(!outOfBounds(j, i+1)){
                    arrAlt[i+1][j] = '.';
                }
                
                if(!outOfBounds(j, i-1)){
                    arrAlt[i-1][j] = '.';
                }
            }
        }
    }
    
    return arrAlt;
}