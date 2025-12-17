class Cell() {
    public:
        Cell(int x, int y) : x_(x), y_(y) {}
        int getX() const { return x_; }
        int getY() const { return y_; }
    private:
        int x_;
        int y_;
};