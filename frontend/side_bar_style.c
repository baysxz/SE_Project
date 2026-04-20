#sidebar {
  width: 280px;
  min-width: 280px;
  background: linear-gradient(180deg, #1a2a4a 0%, #243b6b 100%);
  color: #fff;
  box-shadow: 2px 0 8px rgba(0,0,0,0.15);
}

#sidebar-nav::-webkit-scrollbar { width: 4px; }
#sidebar-nav::-webkit-scrollbar-track { background: transparent; }
#sidebar-nav::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.2); border-radius: 2px; }

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 22px;
  cursor: pointer;
  transition: background 0.2s, border-left 0.2s;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background: rgba(255,255,255,0.08);
}

.nav-item.active {
  background: rgba(255,255,255,0.15);
  border-left: 3px solid #4a90d9;
}

.nav-num {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
  min-width: 18px;
  margin-top: 1px;
}

.nav-item.active .nav-num {
  color: rgba(255,255,255,0.8);
}

.nav-label {
  font-size: 13px;
  line-height: 1.45;
  color: rgba(255,255,255,0.75);
  font-weight: 400;
}

.nav-item.active .nav-label {
  color: #fff;
  font-weight: 600;
}
