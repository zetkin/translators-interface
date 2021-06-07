import React, { useState } from 'react'
import { fade } from '@material-ui/core/styles'

import { InputBase, Button, Tooltip } from '@material-ui/core'

import theme from '../../styles/theme'

import { AUTHOR_NAME_LOCAL_STORAGE_KEY } from '../constants'
import useLocalStorage from '../hooks/useLocalStorage'
import isEmail from '../utils/isEmail'

const EmailField = () => {
  const [authorEmail, setAuthorEmail] = useLocalStorage<string>(
    AUTHOR_NAME_LOCAL_STORAGE_KEY
  )
  const [value, setValue] = useState<string>(authorEmail)
  const [error, setError] = useState<boolean>()

  const handleSave = () => {
    if (!error) {
      setAuthorEmail(value)
    }
  }

  return (
    <div style={{ display: 'flex' }}>
      <div
        style={{
          backgroundColor: fade(theme.palette.common.white, 0.15),
          color: theme.palette.common.white,
          borderRadius: 4,
          padding: theme.spacing(0.25, 2),
        }}
      >
        <InputBase
          placeholder="Your email..."
          style={{ color: 'inherit' }}
          value={value}
          onChange={(e) => {
            // Set current value
            setValue(e.target.value)
            // Check if error
            setError(!isEmail(e.target.value))
          }}
        />
      </div>
      {
        // If current value different than saved value
        value != authorEmail && (
          <Tooltip
            title="Email address not valid"
            disableFocusListener
            disableHoverListener
            disableTouchListener
            arrow
            open={error}
          >
            <Button
              disabled={error}
              style={{
                backgroundColor: fade(theme.palette.common.white, 0.15),
                color: theme.palette.common.white,
                borderRadius: 4,
                padding: theme.spacing(0.25, 2),
                marginLeft: '5px',
              }}
              variant="contained"
              disableElevation
              onClick={handleSave}
            >
              Save
            </Button>
          </Tooltip>
        )
      }
    </div>
  )
}

export default EmailField
