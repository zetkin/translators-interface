import React, { useState } from 'react'

import {
  Modal,
  Paper,
  Container,
  Link,
  Typography,
  Divider,
  TextField,
  Button,
  Tooltip,
} from '@material-ui/core'

import useLocalStorage from '../hooks/useLocalStorage'
import isEmail from '../utils/isEmail'

import { AUTHOR_NAME_LOCAL_STORAGE_KEY } from '../constants'

interface Props {
  open: boolean
  onClose: () => void
}

const RegisterDialog = ({ open, onClose }: Props) => {
  const [authorEmail, setAuthorEmail] = useLocalStorage<string>(
    AUTHOR_NAME_LOCAL_STORAGE_KEY
  )
  const [value, setValue] = useState<string>(authorEmail)
  const [error, setError] = useState<boolean>()

  return (
    <Modal open={open} onClose={onClose}>
      <Container maxWidth="xs">
        <Paper
          style={{
            marginTop: '20vh',
            padding: 20,
          }}
        >
          <Typography variant="h5">
            Please provide your email address.
          </Typography>
          <Typography variant="body1" style={{ marginTop: 15 }}>
            We need your email address to avoid spam, and to be able to contact
            you in the future regarding new translations. If you ever want us to
            delete your email address from our records, please contact{' '}
            <Link href="mailto:info@zetkin.org">info@zetkin.org</Link>
          </Typography>

          <Divider style={{ margin: '15px 0 20px 0' }} />

          <TextField
            style={{ width: '100%' }}
            variant="outlined"
            label="Your email address"
            color="secondary"
            onChange={(e) => {
              // Set current value
              setValue(e.target.value)
              // Check if error
              setError(!isEmail(e.target.value))
            }}
          />
          <Tooltip
            title="Email address not valid"
            disableFocusListener
            disableHoverListener
            disableTouchListener
            arrow
            open={error && value && value.length > 0}
          >
            <Button
              disabled={error || !value?.length}
              variant="contained"
              color="secondary"
              fullWidth
              style={{ marginTop: 10 }}
              value={value}
              onClick={() => {
                setAuthorEmail
              }}
            >
              Submit
            </Button>
          </Tooltip>
        </Paper>
      </Container>
    </Modal>
  )
}

export default RegisterDialog
