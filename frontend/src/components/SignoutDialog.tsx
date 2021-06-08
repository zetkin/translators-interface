import React, { useContext } from 'react'

import {
  Modal,
  Paper,
  Container,
  Typography,
  Button,
  Divider,
} from '@material-ui/core'

import { UserEmailContext } from '../contexts/userEmailContext'

interface Props {
  open: boolean
  onClose: () => void
}

const SignoutDialog = ({ open, onClose }: Props) => {
  const { setUserEmail } = useContext(UserEmailContext)

  return (
    <Modal open={open} onClose={onClose}>
      <Container maxWidth="xs">
        <Paper
          style={{
            marginTop: '20vh',
            padding: 20,
          }}
        >
          <Typography variant="h5">Sign out</Typography>

          <Typography variant="body1" style={{ marginTop: 15 }}>
            To sign back in, simply enter your email again.
          </Typography>

          <Divider style={{ margin: '15px 0 20px 0' }} />

          <Button
            variant="contained"
            color="primary"
            fullWidth
            onClick={() => {
              setUserEmail(null)
              onClose()
            }}
          >
            Sign Out
          </Button>
        </Paper>
      </Container>
    </Modal>
  )
}

export default SignoutDialog
