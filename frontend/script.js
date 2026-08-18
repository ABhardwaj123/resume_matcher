const submitBtn = document.getElementById('submitBtn')

submitBtn.addEventListener('click' , async () => {
    const resumeFile = document.getElementById('resume').files[0]
    const jdText = document.getElementById('jdText').value

    const formData = new FormData()
    formData.append('resume' , resumeFile)
    formData.append('jd_text' , jdText)

    const response = await fetch('http://127.0.0.1:8000/match' , {
        method: 'POST',
        body: formData
    })

    const data = await response.json()
    
    document.getElementById('score').textContent = data.score

    const matchedList = document.getElementById('matchedList')
    matchedList.innerHTML = ''
    data.matchedSkills.forEach(skill => {

        const li = document.createElement('li')
        li.textContent = skill
        matchedList.appendChild(li)
    })


    const missingList = document.getElementById('missingList')
    missingList.innerHTML = ''
    data.missingSkills.forEach(skill => {
        const li = document.createElement('li')
        li.textContent = skill
        missingList.appendChild(li)
    })

    document.getElementById('results').style.display = 'block'
})

