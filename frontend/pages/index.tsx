import { GetServerSideProps, NextPage } from 'next'
import Head from 'next/head'

import { Container, Typography } from '@material-ui/core'

import { EN_LANGUAGE_CODE } from '../src/constants'
import { Project } from '../src/global.types'
import { getProjects } from '../src/api/projects'
import ProjectCard from '../src/components/ProjectCard'

/**
 * Home Page - Lists Projects
 */

interface StaticProps {
  projects: Project[]
}

export const getServerSideProps: GetServerSideProps<StaticProps> = async () => {
  const projects = await getProjects()
  return { props: { projects } }
}

const Home: NextPage<StaticProps> = ({ projects }) => {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta
          name="description"
          content="Contribute to the localisation of Zetkin's software"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container style={{ marginTop: 40, marginBottom: 20 }}>
          <Typography variant="h3" component="h1" style={{ marginBottom: 40 }}>
            Projects
          </Typography>

          <div
            style={{
              display: 'grid',
              gridTemplateColumns: '1fr 1fr 1fr',
              gridTemplateRows: 'auto',
              alignItems: 'center',
              gridGap: 20,
            }}
          >
            {/* Projects */}
            {projects.map((project) => {
              // Only show project if it has English configured and has been synced
              if (
                project.languages.some(
                  (language) => language.language_code === EN_LANGUAGE_CODE
                ) &&
                project.last_sync_time != null
              ) {
                return <ProjectCard project={project} />
              }
            })}
          </div>
        </Container>
      </main>
    </div>
  )
}

export default Home
