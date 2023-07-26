from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

class BoardState:
    def __init__(self):
        self.action_cubes = 0
        self.bird_hand = []
        self.bonus_hand = []
        # ... add other class variables ...

    # ... add methods to update class variables ...

# Create an instance of the BoardState class
board_state_instance = BoardState()

@app.route('/')
def index():
    return render_template('gameboard.html', board_state=board_state_instance)

@app.route('/get_board_state', methods=['GET'])
def get_board_state():
    # Return the board_state_instance as JSON
    return jsonify(vars(board_state_instance))

@app.route('/update_action_cubes', methods=['POST'])
def update_action_cubes():
    data = request.get_json()
    action_cubes = data.get('action_cubes')
    # Update the action_cubes value in the board_state_instance
    board_state_instance.action_cubes = action_cubes
    return jsonify({'message': 'Action cubes updated successfully'})

# Add similar routes and functions to handle updates for other class variables

if __name__ == '__main__':
    app.run(debug=True)
