import '../css/Header.css';
const Header = () => {
  return ( 
  <header>
    <nav className="nav">
      {/* id="page-logo" -> className="site-title" */}
      <a href="./" className="site-title">MAV</a>
        <ul>
          <li>
            <a href="./activities">ACTIVITIES</a>
          </li>
          <li>
            <a href="./members">MEMBERS</a>
          </li>
          <li>
            <a href="./recruitment">RECRUITMENT</a>
          </li>
        </ul>

    </nav>
  </header>
  )
}

export default Header;