// Sample celebrity data (can be replaced with an API call)
const celebrities = [
    {
      name: "Leonardo DiCaprio",
      image: "images/leonardo.jpg",
      bio: "Academy Award-winning actor known for Titanic and Inception.",
      profession: "Actor"
    },
    {
      name: "Taylor Swift",
      image: "images/taylor.jpg",
      bio: "Grammy-winning singer-songwriter with multiple chart-topping albums.",
      profession: "Musician"
    },
    {
      name: "Cristiano Ronaldo",
      image: "images/ronaldo.jpg",
      bio: "One of the greatest footballers of all time.",
      profession: "Athlete"
    },
    {
      name: "Scarlett Johansson",
      image: "images/scarlett.jpg",
      bio: "Actress known for her roles in Marvel movies and Lost in Translation.",
      profession: "Actor"
    }
  ];
  
  // DOM Elements
  const grid = document.querySelector('.celebrity-grid');
  const searchInput = document.getElementById('search');
  const professionFilter = document.getElementById('profession-filter');
  const prevPageButton = document.getElementById('prev-page');
  const nextPageButton = document.getElementById('next-page');
  const pageInfo = document.getElementById('page-info');
  const modal = document.getElementById('modal');
  const modalImage = document.getElementById('modal-image');
  const modalName = document.getElementById('modal-name');
  const modalBio = document.getElementById('modal-bio');
  const closeModal = document.querySelector('.close');
  const themeToggle = document.querySelector('.theme-toggle');
  
  // Pagination
  let currentPage = 1;
  const itemsPerPage = 4;
  
  // Theme Toggle
  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('light-mode');
  });
  
  // Display celebrities
  function displayCelebrities(celebrities, page = 1) {
    grid.innerHTML = '';
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const paginatedCelebrities = celebrities.slice(start, end);
  
    paginatedCelebrities.forEach(celebrity => {
      const card = document.createElement('div');
      card.classList.add('celebrity-card');
  
      card.innerHTML = `
        <img src="${celebrity.image}" alt="${celebrity.name}">
        <h3>${celebrity.name}</h3>
      `;
  
      card.addEventListener('click', () => {
        openModal(celebrity);
      });
  
      grid.appendChild(card);
    });
  
    // Update pagination buttons
    prevPageButton.disabled = page === 1;
    nextPageButton.disabled = end >= celebrities.length;
    pageInfo.textContent = `Page ${page} of ${Math.ceil(celebrities.length / itemsPerPage)}`;
  }
  
  // Open modal with celebrity details
  function openModal(celebrity) {
    modalImage.src = celebrity.image;
    modalName.textContent = celebrity.name;
    modalBio.textContent = celebrity.bio;
    modal.style.display = 'block';
  }
  
  // Close modal
  closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
  });
  
  // Filter and search functionality
  function filterCelebrities() {
    const searchTerm = searchInput.value.toLowerCase();
    const profession = professionFilter.value;
  
    const filteredCelebrities = celebrities.filter(celebrity => {
      const matchesSearch = celebrity.name.toLowerCase().includes(searchTerm);
      const matchesProfession = profession ? celebrity.profession === profession : true;
      return matchesSearch && matchesProfession;
    });
  
    displayCelebrities(filteredCelebrities, currentPage);
  }
  
  // Event listeners
  searchInput.addEventListener('input', filterCelebrities);
  professionFilter.addEventListener('change', filterCelebrities);
  prevPageButton.addEventListener('click', () => {
    currentPage--;
    filterCelebrities();
  });
  nextPageButton.addEventListener('click', () => {
    currentPage++;
    filterCelebrities();
  });
  
  // Initial display
  displayCelebrities(celebrities);