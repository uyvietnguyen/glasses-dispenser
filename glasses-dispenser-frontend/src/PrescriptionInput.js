import React, { Component } from 'react';

class PrescriptionInput extends Component {
  render() {
    return(
      <div>
        <form>
          <p>Right Prescription</p>
          <input type="text"/>
          <p>Left Prescription</p>
          <input type="text"/>

          <div>
            <input type="submit" value="Submit" />
          </div>
        </form>
      </div>
    )
  }
}

export default PrescriptionInput;